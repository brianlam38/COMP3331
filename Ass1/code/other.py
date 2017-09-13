#!/usr/bin/python3
import sys
from stp_packet import STPPacket
import pickle
import socket
import time
import itertools
from pld_module import PacketThrottler
from threading import Timer
import random as r
 
timer_flag = True
# verbose_flag = True
 
verbose_flag = False
 
 
class Sender:
    def __init__(self, receiver_host_ip, receiver_port, mws, mss,
                 timeout_length, pdrop, seed_value):
        self.receiver_host_ip = receiver_host_ip
        self.receiver_port = receiver_port
        self.timeout_length = timeout_length
        self.buffer_size = 4096
        self.connection_socket = self.open_connection()
        self.packet_buffer = {}
        self.log_name = "Sender_log.txt"
        open(self.log_name, 'w').close()  # clear old log
        # Base asst, no packet delay
        self.run_stats = {
            "bytes_sent": 0,
            "segments_sent": 0,
            "duplicates_sent": 0,
            "packets_dropped": 0,
            "duplicates_ack": 0
        }
        self.run_stats_msgs = {
            "bytes_sent":
            'Amount of (original) Data Transferred (in bytes) {}\n',
            "segments_sent":
            'Number of  Data Segments Sent (excluding retransmissions) {}\n',
            "packets_dropped":
            'Number of (all) Packets Dropped {}\n',
            "duplicates_sent":
            'Number of Retransmitted Segments {}\n',
            "duplicates_ack":
            'Number of Duplicate Acknowledgements received {}\n'
        }
        self.receiver_seq_num = 0  # Set by synack packet
        self.mss = mss
        self.mws = mws
        self.prev_duplicates_received = 0
        self.sender_timer = None
        self.pld = PacketThrottler(seed_value, pdrop)
        self.init_seq_num = self.pld.get_random_init_seq_num()
        self.next_seq_num = self.init_seq_num
        self.send_base = self.next_seq_num
        self.syn_flag = False
        self.fin_flag = False
        self.send_flag = False
        self.start_time = time.time()  # count time from connection start
 
    # specify timeout_length. if this fails then calls stp.retransmit(seq_num)
    # TODO figure out timeout; get from packet buffer?
 
    def open_connection(self):
        try:
            connection_socket = socket.socket(socket.AF_INET,
                                              socket.SOCK_DGRAM)
            return connection_socket
        except socket.error:
            print("Failed to create socket")
            sys.exit()
 
    def close_connection(self):
        """
       sender teardown operations: close socket, make final log
       """
 
        if verbose_flag: print("Inside close connection, about to shut down")
        if timer_flag:
            self.sender_timer.cancel()  # about to finish, stop timer
        self.connection_socket.close()
        self.close_log()
 
    def send_packet(self, stp_packet):
        self.next_seq_num += len(stp_packet.data)
        if verbose_flag:
            print(
                "About to attempt sending packet seq num: {}, send_base: {}, next_seq_num: {}".
                format(stp_packet.seq_num, self.send_base, self.next_seq_num))
        send_type = self.get_packet_type(stp_packet)
        self.packet_buffer[stp_packet.seq_num] = stp_packet
 
        if self.pld.should_transmit_packet() or self.syn_flag or self.fin_flag:
            if verbose_flag:
                print(
                    "About to send pkt seq num: {}, ack_num: {}, send_base: {}, next_seq_num: {}".
                    format(stp_packet.seq_num, stp_packet.ack_num,
                           self.send_base, self.next_seq_num))
            self.connection_socket.sendto(
                pickle.dumps(stp_packet), (self.receiver_host_ip,
                                           self.receiver_port))
            action_type = 'snd'
 
        else:
            if not (self.syn_flag or self.fin_flag):
                action_type = 'drop'
 
        # if packet is dropped, we always reset timer?
        # eitherwise, skip if there is a timer already running
        if not (self.syn_flag or self.fin_flag) and timer_flag:
            # if (self.sender_timer is
            #        None) or (not self.sender_timer.is_alive()):
            self.set_timer()
            # start the timer
            if verbose_flag:
                print("starting timer. synflag: {}, fin_flag: {}".format(
                    self.syn_flag, self.fin_flag))
            self.sender_timer.start()
        self.update_log(action_type, send_type, stp_packet)
 
    def retransmit_packet(self, seq_num):
        if verbose_flag:
            print("timer expired: about to retransmit seq num: {}".format(
                seq_num))
        retransmit_packet = self.packet_buffer[seq_num]
        if self.pld.should_transmit_packet() or self.syn_flag or self.fin_flag:
            self.connection_socket.sendto(
                pickle.dumps(retransmit_packet), (self.receiver_host_ip,
                                                  self.receiver_port))
            action_type = 'snd'
        else:
            action_type = 'drop'
        self.set_timer()
        # start the timer
        if verbose_flag:
            print("starting timer")
        self.run_stats["duplicates_sent"] += 1
        send_type = self.get_packet_type(retransmit_packet)
        self.update_log(
            action_type, send_type, retransmit_packet, is_retransmit='RT')
        self.sender_timer.start()
        self.send_flag = False
 
    def receive_synack(self):
        data, addr = self.connection_socket.recvfrom(self.buffer_size)
        stp_packet = pickle.loads(data)  # data is property of stp_packet
        if verbose_flag:
            print("Sender Received packet. addr: {}".format(addr))
            stp_packet.print_properties()
        if stp_packet.syn and stp_packet.ack and stp_packet.ack_num > self.send_base:
            self.receiver_seq_num = stp_packet.seq_num
            self.update_log('rcv', self.get_packet_type(stp_packet),
                            stp_packet)
            # ack_num will be 1 more than last acked byte
            self.process_ack(self.send_base)
            self.send_base = stp_packet.ack_num
            return True
        return False
 
    def receive_fin_ack(self):
        data, addr = self.connection_socket.recvfrom(self.buffer_size)
        stp_packet = pickle.loads(data)  # data is property of stp_packet
        if stp_packet.ack and stp_packet.fin:
            self.process_ack(self.next_seq_num)
            self.update_log('rcv', self.get_packet_type(stp_packet),
                            stp_packet)
            return True
        return False
 
    def receive_packet(self):
        """
       Returns boolean signifying whether received packet is
       the next expected one
       """
        data, addr = self.connection_socket.recvfrom(self.buffer_size)
        stp_packet = pickle.loads(data)  # data is property of stp_packet
        if verbose_flag:
            print("Sender Received packet. addr: {}".format(addr))
            stp_packet.print_properties()
        received_ack = stp_packet.ack_num
        if stp_packet.ack:  # we received an ack
            if received_ack > self.send_base:
                self.sender_timer.cancel(
                )  # stop timer on prev packet, new base
                self.update_log('rcv',
                                self.get_packet_type(stp_packet), stp_packet)
                # ack_num will be 1 more than last acked byte
                self.send_base = received_ack
                # stop tracking any newly acked packets
                if verbose_flag:
                    print("""cur sendbase: {}, cur next_seq_num: {}
                                       """
                          .format(self.send_base, self.next_seq_num))
 
                if verbose_flag:
                    print("""received packet with ack_num: {}
                           there are still unacknowledged packets: {},
                           pre-key removal
                       """.format(received_ack, self.packet_buffer.keys()))
 
                keys_to_remove = [
                    key for key in self.packet_buffer.keys()
                    if key < self.send_base
                ]
                for key in keys_to_remove:
                    self.process_ack(key)
                if timer_flag and self.sender_timer is not None:
                    self.sender_timer.cancel()
 
                if len(self.packet_buffer) > 0:
                    if verbose_flag:
                        print("""received packet with ack_num: {}
                           there are still unacknowledged packets: {},
                           resetting timer
                       """.format(received_ack, self.packet_buffer.keys()))
                    self.set_timer()
                    if timer_flag:
                        self.sender_timer.start()
                return True
            else:
                if verbose_flag:
                    print("triggered duplicates!")
                self.prev_duplicates_received += 1
                self.run_stats["duplicates_ack"] += 1
                self.update_log('rcv',
                                self.get_packet_type(stp_packet), stp_packet,
                                'RTA')
                if self.prev_duplicates_received == 3:
                    self.prev_duplicates_received = 0  # reset
                    self.retransmit_packet(self.send_base)
        return False
 
    # current waiting ack received; cancel timer
    def process_ack(self, seq_num):
        del (self.packet_buffer[seq_num])
        if verbose_flag:
            print("just deleted {} from packet_buffer".format(seq_num))
        # if unacknowledged segments exist, start again?
 
    def process_file(self, file_path):
        # file.txt is closed after open
        with open(file_path, 'rb') as handle:
            self.file_bytes = list(handle.read())
 
    def get_packet_data_size(self):
        # TODO do min(mss, mws) - sizeof empty packet object
        # n segments = int(len(self.file_bytes) / self.mss)
        # if there isn't enough space
        if self.mss < self.mws:
            available_window_bytes = self.mws - self.get_cur_window_size()
            if available_window_bytes > 0:
                if available_window_bytes >= self.mss:
                    return self.mss  # if there's space, send max segment
                else:
                    return available_window_bytes  # otherwise send what's left
            else:
                raise ValueError(
                    'Trying to get packet data size to make new packet with no window space'
                )
        else:
            return self.mws  # if window is smaller, just saturate the window
 
    def get_packet_data(self, num_bytes):
        # get bytes, remove from bytes left to send
        packet_bytes = self.file_bytes[:num_bytes]
        self.file_bytes = self.file_bytes[num_bytes:len(self.file_bytes)]
        return packet_bytes
 
    def get_cur_window_size(self):
        if verbose_flag:
            print("window size is: {}, send_base: {}, next_seq_num: {}".format(
                (self.next_seq_num - self.send_base
                 ), self.send_base, self.next_seq_num))
        # return max of window and 0 to force >= 0
        return max((self.next_seq_num - self.send_base), 0)  # (-1's cancel)
 
    def form_stp_packet(self):
        """
       creates a new unique stp packet for sending and saves state with sender
       """
        if verbose_flag:
            print("Form_STP_packet: About to get packet data size")
        packet_data_size = self.get_packet_data_size()
        if verbose_flag:
            print("Form_STP_packet: About to get packet contents of size: {}".
                  format(packet_data_size))
        packet_data = self.get_packet_data(
            packet_data_size)  # use constant in init
        # does sender need to include an ack_num? unidirectional? check..
        new_packet = STPPacket(
            bytes(packet_data), self.next_seq_num, self.receiver_seq_num)
 
        return new_packet
 
    def update_log(self,
                   packet_action,
                   packet_type,
                   stp_packet,
                   is_retransmit='O'):
        if is_retransmit == 'RT':
            self.run_stats["duplicates_sent"] += 1
        elif packet_action == "ack" and is_retransmit == 'RTA':
            self.run_stats["duplicates_ack"] += 1
        if packet_action == "drop":
            self.run_stats["packets_dropped"] += 1
        time_since_excution = (time.time() - self.start_time) * 1000  # ms
        with open(self.log_name, 'a') as handle:
            handle.write('{} {} {} {} {} {}\n'.format(
                packet_action, time_since_excution, packet_type,
                stp_packet.seq_num, len(stp_packet.data), stp_packet.ack_num))
 
    def close_log(self):
        if verbose_flag:
            print('About to close off log')
        with open(self.log_name, 'a') as handle:
            for key in self.run_stats_msgs:
                handle.write(self.run_stats_msgs[key]
                             .format(self.run_stats[key]))
 
    # always sends send_base
    def set_timer(self):
        if self.sender_timer is not None:
            self.sender_timer.cancel()
        min_not_acked_seq_num = self.send_base
        if timer_flag:
            self.sender_timer = Timer(
                self.timeout_length,
                self.retransmit_packet,
                args=[min_not_acked_seq_num])
 
    def set_close_timer(self, timeout_length):
        if verbose_flag:
            print("About to set close connection timer of length: {}".format(
                timeout_length))
 
        if self.sender_timer is not None:
            self.sender_timer.cancel()
        if timer_flag:
            self.sender_timer = Timer(timeout_length, self.close_connection)
            self.sender_timer.start()
 
    def get_packet_type(self, stp_packet):
 
        if len(stp_packet.data) > 0:
            return 'D'
        else:
            result = ''
            if stp_packet.fin:
                result += 'F'
            elif stp_packet.syn:
                result += 'S'
            if stp_packet.ack:
                result += 'A'
            return result
 
    def initiate_stp(self):
        self.syn_flag = True  # toggle ignore pld
        # copy example log of 0 beginning ack
        init_packet = STPPacket(b'', self.init_seq_num, 0, syn=True)
        # send SYN packet; timer will handle retransmits
        self.next_seq_num += 1  # increment next packet number even though 0 data sent
        self.send_packet(init_packet)
        # SYN_SENT beyond this point
        print('===== SYN_SENT; waiting for response ====')
        while not self.receive_synack():  # wait for SYNACK packet
            pass
        self.receiver_seq_num += 1  # synack processed, first packet sent will do acknowledging
        # send ACK to SYNACK with no data; timer handles retransmit
        self.send_packet(
            STPPacket(b'', self.next_seq_num, self.receiver_seq_num, ack=True))
        # ESTABLISHED beyond this point
        self.syn_flag = False  # next packets will not ignore pld
        print('===== STP CONNECTION ESTABLISHED ====')
 
    def close_stp(self):
        self.fin_flag = True  # start ignoring pld again for close
        fin_packet = STPPacket(
            b'', self.next_seq_num, self.receiver_seq_num, fin=True)
        # send SYN packet; timer will handle retransmits
        if verbose_flag:
            print("About to send fin packet")
        self.send_packet(fin_packet)
        # FIN_WAIT_1 beyond this point
        # FIN_WAIT_2 beyond this point
        print('===== STP CLOSE INITIATED: fin sent ====')
        if verbose_flag:
            print("About to wait on fin ack packet")
        while not self.receive_fin_ack():  # wait for SYNACK packet
            pass
        if verbose_flag:
            print("About to ack receiver finack packet")
        ack_packet = STPPacket(
            b'', self.next_seq_num, self.receiver_seq_num, ack=True)
        self.send_packet(ack_packet)
        # TIME_WAIT beyond tthis point
        # override default timer; close down after input timeout
        self.set_close_timer(self.timeout_length)
        print('===== STP CONNECTION CLOSED ====')
        self.fin_flag = False  # stop ignoring pld (even though program is ending)
 
 
if __name__ == "__main__":
    # TODO event loop question... setting varialbes in init method instead of after synack ok?
    # TODO textbook says sender ack carries payload, spec example does not. which one?
    # python sender.py receiver_host_ip receiver_port file.txt MWS MSS
    # MWS: max window size in bytes
    # MSS: max segmet size (max data in bytes carried in each STP_packet)
    # pdrop: probability to drop 0-1, seed: seed for rgeerator
    # use the same socket for send packets/receiver ack - acks bypass pld
    n_expected_args = 9
    if verbose_flag:
        print("Setup sender")
    if len(sys.argv) < n_expected_args:
        print(
            """Usage: python sender.py receiver_host_ip receiver_port file.txt
               MWS MSS timeout pdrop seed""")
    else:
 
        receiver_host_ip, receiver_port, file_path, \
                mws, mss, timeout, pdrop, seed_value = sys.argv[1:]
        sender = Sender(
            receiver_host_ip,
            int(receiver_port),
            int(mws),
            int(mss),
            float(timeout) / 1000,  # timeout input convert ms to s
            float(pdrop),
            int(seed_value))
        sender.process_file(file_path)
        if verbose_flag:
            print("Sender setup, connection opened details: {}".format(
                sender.connection_socket.getsockname()))
        # Operate webserver whilst there is stuff left to transfer
        # OR still waiting for acks
        # loop inside intiate until success
        sender.initiate_stp()
        while len(sender.file_bytes) > 0 or len(
                sender.packet_buffer.keys()) > 0:
            sender.send_flag = True
            while (int(mws) - sender.get_cur_window_size()
                   ) > 0 and len(sender.file_bytes) > 0:  # send one at a time
                if verbose_flag:
                    print("Entered send loop, about to send packet data")
                cur_packet = sender.form_stp_packet()
                sender.run_stats["bytes_sent"] += len(cur_packet.data)
                sender.run_stats["segments_sent"] += 1
                sender.send_packet(cur_packet)
                if verbose_flag:
                    print(
                        "Just sent packet data: {}, bytes left: {}, sender.send_base: {}, sender.next_seq_num: {}".
                        format(cur_packet.data,
                               len(sender.file_bytes), sender.send_base,
                               sender.next_seq_num))
                sender.send_flag = False
            # sent packet, change into ack wait mode
            if verbose_flag:
                print("After send loop, about to receive packet data")
            while not sender.receive_packet():
                pass
 
        if verbose_flag:
            print(
                "All packets sent - no more packet sending, close connection")
        sender.close_stp()
        # TODO questions:
        # 1. structure 2. pick seq # starting, pick ack from sender?
        # does connection die after JUST transfer the file? when to close?
        # MSS / MWS determine how big chunks to break file into?
        # ^ calculate size of total packet, then just put data in to fill?
        # sender should send acks to say it's received
        # pick random for start