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
		data, client_addr = self.socket.recvfrom(2048)
		stp_packet = pickle.loads(data)
		return stp_packet, client_addr

	# add payload to final file
	def append_payload(self, data):
		print("data = {}".format(data))
		f = open("r_test.txt", "a+")
		f.write(data)
		f.close()

	# create SYNACK
	def make_SYNACK(self, seq_num, ack_num):
		print("Creating SYNACK")
		SYNACK = STPPacket('SYNACK', seq_num, ack_num, ack=True, syn=True, fin=False)
		return SYNACK

	# create ACK
	def make_ACK(self, seq_num, ack_num):
		print("Creating ACK")
		ACK = STPPacket('ACK', seq_num, ack_num, ack=True, syn=False, fin=False)
		return ACK

	# create FIN
	def make_FIN(self, seq_num, ack_num):
		print("Creating FIN")
		FIN = STPPacket('FIN', seq_num, ack_num, ack=False, syn=False, fin=True)
		return FIN

	# send segment over UDP
	def udp_send(self, packet, addr):
		self.socket.sendto(pickle.dumps(packet), addr)

	# FIN close
	def stp_close(self):
		print("Connection closed")
		self.socket.close()

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
	# init seq ack numbers
	seq_num = 0
	ack_num = 0
	client_addr = None
	# receiver states
	state_listen = True
	state_syn_rcv = False
	state_synack_sent = False
	state_established = False
	# grab args, create socket, bind and create log.txt
	port, file = sys.argv[1:]
	receiver = Receiver(port, file)
	receiver.socket.bind(('', receiver.port))
	print("Receiver is ready ...")
	log = open("Receiver_log.txt","w")

	### MAIN EVENT LOOP ###
	while True:
		print("start of loop")

		### LISTENING STATE ###
		# wait for SYN seg
		if state_listen == True:
			print("STATE: LISTEN")
			syn_pkt, client_addr = receiver.stp_rcv()
			# creating SYNACK
			if syn_pkt.syn == True:
				synack_pkt = receiver.make_SYNACK(seq_num, ack_num)
				receiver.udp_send(synack_pkt, client_addr)
				state_synack_sent = True
				state_listen = False

		### SYNACK SENT ###
		# wait for ACK seg
		if state_synack_sent == True:
			print("STATE: SYNACK SENT")
			ack_pkt, client_addr = receiver.stp_rcv()
			# ACK received, 3-way-established
			if ack_pkt.ack == True:
				state_established = True
				state_synack_sent = False

		### HANDSHAKE ESTABLISHED ###
		if state_established == True:
			print("STATE: CONNECTION ESTABLISHED")
			# grab packets until FIN close request by client
			while True:
				packet, client_addr = receiver.stp_rcv()
				data = packet.data
				# Receive FIN, init close
				if packet.fin == True:
					# send ACK
					ack_pkt = receiver.make_ACK(seq_num, ack_num)
					receiver.udp_send(ack_pkt, client_addr)
					state_end = True
					state_established = False
					break
				# Receive normal seg, add payload to final file
				else:
					print("Packet Payload = {}".format(data))
					receiver.append_payload(data)

		### END OF CONNECTION ###
		if state_end == True:
			print("STATE: END OF CONNECTION")
			# send FIN
			fin_pkt = receiver.make_FIN(seq_num, ack_num)
			receiver.udp_send(fin_pkt, client_addr); print("Sending FIN")
			# wait for ACK
			ack_pkt, client_addr = receiver.stp_rcv()
			# receive ack, close connection
			if ack_pkt.ack == True:
				receiver.stp_close()
				break

	print("Current file content:\n")
	f = open("r_test.txt","r")
	print(f.read())
	# everything finished -> close connection


# on receive
# The receiver should generate ACK immediately after receiving a data segment
#self.timer.cancel()



# 1. Sender waits for data to be passed down from app layer
# 		wait()
# 2. stp_send(data) is called by app layer.
# 3. sender creates packet sndpkt + checksum
# 		stp_send(data)
# 4. send packet via. udp_send
# 		udp_send()
'''
# On packet arrival, receiver replies with ACK/NAK depending on if packet is corrupted
Corrupted = stp_rcv(rcvpkt) && corrupt()
#     -> send NAK packet via. udp_send()
Uncorrupted = rdt_rcv(rcvpkt) && notCorrupt()
#     -> cont. to next step

# Extract data
extract()

# Deliver data to upper layer
deliver()

# Send ACK packet back
udt_send()




# wait for ACK packet -> ACK comes back
# if waiting, can't receive more data from app layer = stp_send() can't occur
# if ACK, go back to waiting for data from app layer
stp_rcv(rcvpkt) && isACK


# wait for ACK packet -> NAK comes back
# if waiting, can't receive more data from app layer = stp_send() can't occur
# if NAK, retransmit last packet + wait for ACK again
stp_rcv(rcvpkt) && isNAK

'''




