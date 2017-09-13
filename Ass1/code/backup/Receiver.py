#!/usr/bin/python

# Simple Transport Protocol (STP)
# Receiver side program
#
# Author: Brian Lam

# Sender -> Packet (seq = 10) -> Receiver
# if match seq number
# 		keep packet
#		send back ACK indicating next packet with 10 + len(data)
# else
#		discard packet (or buffer)

# Example: Sender
# (seq 1) get ACK 11 -> send which packet to repeat
# (seq 11)
# (seq 21)

import pickle
import sys
import time
from socket import *

class STPPacket:
	def __init__(self, data, seq_num, ack_num, ack=False, syn=False, fin=False):
		self.data = data
		self.seq_num = seq_num
		self.ack_num = ack_num
		self.ack = ack
		self.syn = syn
		self.fin = fin

class Receiver:
	# receiver needs to have a sequence number so it can deal with out-of-order pakes
	# receiver receives stp_packet and then writes the data inside the packet

	# initialise receiver data
	def __init__(self, port, file):
		self.port = int(port)
		self.file = file

	# create UDP socket
	socket = socket(AF_INET, SOCK_DGRAM)

	# receive packet from sender, return pkt + client address
	def stp_rcv(self):
		print("waiting for file . . .")
		data, client_addr = self.socket.recvfrom(2048)
		stp_packet = pickle.loads(data)
		return stp_packet, client_addr

	# add payload to final file
	def append_payload(self, data):
		print("Appending packet payload = {}".format(data))
		f = open("r_test.txt", "a+")
		f.write(data)
		f.close()

	# create SYNACK
	def make_SYNACK(self, seq_num, ack_num):
		print("Creating SYNACK")
		SYNACK = STPPacket('', seq_num, ack_num, ack=True, syn=True, fin=False)
		return SYNACK

	# create ACK
	def make_ACK(self, seq_num, ack_num):
		print("Creating ACK")
		ACK = STPPacket('', seq_num, ack_num, ack=True, syn=False, fin=False)
		return ACK

	# create FIN
	def make_FIN(self, seq_num, ack_num):
		print("Creating FIN")
		FIN = STPPacket('', seq_num, ack_num, ack=False, syn=False, fin=True)
		return FIN

	# send segment over UDP
	def udp_send(self, packet, addr):
		self.socket.sendto(pickle.dumps(packet), addr)

	# FIN close
	def stp_close(self):
		print("Connection closed")
		self.socket.close()

	# Update Receiver_log.txt
	def update_log(self, action, pkt_type, packet):
		print("Updating receiver log . . .")
		# grabbing header fields
		seq = packet.seq_num
		ack = packet.ack_num
		size = len(packet.data)
		# clocking time
		curr_time = time.clock() 	 # temp timer
		curr_time = curr_time * 1000 # convert to MS
		curr_time = str(curr_time); seq = str(seq); size = str(size); ack = str(ack)
		# init arrays of args and col lens
		col_lens = [5, 8, 4, 5, 5, 3]
		args = [action, curr_time, pkt_type, seq, size, ack]
		# build string
		final_str = ""
		counter = 0
		# loop through columns
		for c in col_lens:
			arg_len = len(args[counter])
			space_len = c - arg_len
			space_str = ""
			# add whitespace for each column
			while arg_len < c:
				space_str += " "
				arg_len += 1
			# append each col to line
			final_str += str(args[counter]) + space_str
			counter += 1
		# add newline to final str
		final_str += "\n"
		print(final_str)
		# append complete line to log
		f = open("Receiver_log.txt", "a+")
		f.write(final_str)
		f.close()

###################
# MAIN FUNCTION???
###################

# Check correct usage
num_args = 3
if len(sys.argv) != num_args:
	print("Usage: ./Receiver.py port file.txt")
# Continue to main operation
else:
	### SET UP VARIABLES ###
	# init seq/ack vars
	seq_num = 0
	ack_num = 0
	next_seq_num = 0
	next_ack_num = 0
	# set client addr
	client_addr = None
	# receiver states
	state_listen = True
	state_syn_rcv = False
	state_synack_sent = False
	state_established = False
	# grab args, create socket and bind
	port, file = sys.argv[1:]
	receiver = Receiver(port, file)
	receiver.socket.bind(('', receiver.port))
	# track progress of file sent
	data_progress = 0
	# create buffer
	pkt_buffer = {}
	# reset log and final file
	f = open("Receiver_log.txt", "w")
	f.close()
	f = open("r_test.txt", "w")
	f.close()
	print("Receiver is ready . . .")

	### MAIN EVENT LOOP ###
	while True:
		print("start of loop")

		### LISTENING STATE ###
		# wait for SYN seg
		if state_listen == True:
			print("\n===================== STATE: LISTEN")
			syn_pkt, client_addr = receiver.stp_rcv()
			receiver.update_log("rcv", 'S', syn_pkt)
			# acknowledge client SYN
			ack_num = syn_pkt.seq_num + 1
			# creating SYNACK
			if syn_pkt.syn == True:
				synack_pkt = receiver.make_SYNACK(seq_num, ack_num)
				receiver.udp_send(synack_pkt, client_addr);
				receiver.update_log("snd", 'SA', synack_pkt)
				# increment seq for SYNACK
				seq_num += 1
				state_synack_sent = True
				state_listen = False

		### SYNACK SENT ###
		# wait for ACK seg
		if state_synack_sent == True:
			print("\n===================== STATE: SYNACK SENT")
			ack_pkt, client_addr = receiver.stp_rcv()
			receiver.update_log("rcv", 'A', ack_pkt)

			# ACK received, 3-way-established
			if ack_pkt.ack == True:
				state_established = True
				state_synack_sent = False

		### HANDSHAKE ESTABLISHED ###
		if state_established == True:
			print("\n===================== STATE: CONNECTION ESTABLISHED")
			# grab packets until FIN close request by client
			while True:
				packet, client_addr = receiver.stp_rcv()
				data = packet.data
				# Receive FIN, init close
				if packet.fin == True:
					print("FIN initiated by sender . . .")
					receiver.update_log("rcv", 'F', packet)
					state_end = True
					state_established = False
					break
				# Receive normal seg, check pkt_sn = rcv_sn
				# Send ACK for packet, increment seq_num by sizeof payload
				elif True: #packet.seq_num == seq_num:
					# acknowledge seg, increment seq_num (indicate sizeof payload ack-ing)
					ack_pkt = receiver.make_ACK(seq_num, ack_num)
					receiver.udp_send(ack_pkt, client_addr);
					seq_num += packet.seq_num
					# add payload to final file
					data_progress += len(data)
					receiver.append_payload(data)
					receiver.update_log("rcv", 'D', packet)
				# Out of order packet, put in buffer
				else:
					print("Out of order, put in buffer")

		### END OF CONNECTION ###
		if state_end == True:
			print("\n===================== STATE: END OF CONNECTION ")
			# send ACK + FIN consecutive
			ack_pkt = receiver.make_ACK(seq_num, ack_num)
			receiver.udp_send(ack_pkt, client_addr)
			fin_pkt = receiver.make_FIN(seq_num, ack_num)
			receiver.udp_send(fin_pkt, client_addr)
			receiver.update_log("snd", 'FA', fin_pkt)
			# wait for ACK
			ack_pkt, client_addr = receiver.stp_rcv()
			receiver.update_log("rcv", 'A', ack_pkt)
			# receive ack, close connection
			if ack_pkt.ack == True:
				receiver.stp_close()
				break

	# Print final file
	print("\n### FINAL FILE.TXT CONTENT ###")
	f = open("r_test.txt","r")
	print(f.read())

	# Print final receiver log
	print("\n### FINAL RECEIVER LOG ###")
	f = open("Receiver_log.txt", "r")
	print(f.read())


# on receive
# The receiver should generate ACK immediately after receiving a data segment
#self.timer.cancel()

'''
# wait for ACK packet -> ACK comes back
# if waiting, can't receive more data from app layer = stp_send() can't occur
# if ACK, go back to waiting for data from app layer
stp_rcv(rcvpkt) && isACK


# wait for ACK packet -> NAK comes back
# if waiting, can't receive more data from app layer = stp_send() can't occur
# if NAK, retransmit last packet + wait for ACK again
stp_rcv(rcvpkt) && isNAK
'''



