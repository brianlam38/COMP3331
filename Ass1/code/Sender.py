#!/usr/bin/python

# Simple Transport Protocol (STP)
#
# Sender side program
# 
# Three major components to data transmission and re-transmission:
# 1. Data received from app layer above
# 2. Timer timeout
# 3. ACK receipt

import pickle
import sys
import os
from socket import *

# exe format:
# python sender.py receiver_host_ip receiver_port file.txt MWS MSS timeout pdrop seed

class STPPacket:
	def __init__(self, data, seq_num, ack_num, ack=False, syn=False, fin=False):
		self.data = data
		self.seq_num = seq_num
		self.ack_num = ack_num
		self.ack = ack
		self.syn = syn
		self.fin = fin

class Sender:
	# you need to create this.
	# a lot more complicated, but just follow the assignment spec
	# you can do go-back-N, selective repeat, whatever works
	# also need sequence number

	# create initial seq nums
	init_seq_num = 0
	init_ack_num = 0
	# NextSeqNum = InitialSeqNumber
	# SendBase = InitialSeqNumber

	# initialise sender data: seq number, timeout
	def __init__(self, r_host_ip, r_port, file, MWS, MSS, timeout, pdrop, seed):
		self.r_host_ip = r_host_ip
		self.r_port = int(r_port)
		self.file = file      		# grab file from arg[4]
		self.MWS = MWS				# max window size
		self.MSS = MSS 				# max segment size
		self.timout = timeout
		self.pdrop = pdrop
		self.seed = seed

	# read file from input -> separate into segments -> pop into stack
	# NOTE: max_seg_size = max bytes carried in each STP segment
	#
	# Called by app-layer to pass down data to transport layer.
	def stp_send(self):
		#file = sys.argv[2]		
		file_size = len(self.file) 		# file_size = os.path.getsize(file)
		print(file_size)
		# read file
		# segment = filesize / max_seg_size
		# seg_size

		# preparing data
		f = open(self.file, "r")	# open file
		data = f.read()				# read file + store in data obj
		return data

	# creating stp_packet to send to receiver
	# modify later to create packet based off MSS / MWS
	def make_pkt(self, data):
		stp_packet = STPPacket(data, self.init_seq_num, self.init_ack_num, True, False, False)
		return stp_packet

	# send via. UDP to receiver
	socket = socket(AF_INET, SOCK_DGRAM)
	def udp_send(self, stp_packet):
		# sender explicitly attaches IP destination address and port no. to each packet
		self.socket.sendto(pickle.dumps(stp_packet), (self.r_host_ip, self.r_port))
		#return_msg, server_add = socket.recvfrom(2048)	# receives data from server
		#self.socket.close()

	# FIN close
	def stp_close(self):
		self.socket.close()

# how to create packet?
# myPacket = Packet(data, 0, 0, True, False, False)

# Packet is an object. How to send and receive this over UDP?

# send
#stp_packet = STPPacket(data, . . .)
#socket.sendto(pickle.dumps(stp_packet), (client_ip, client_port))

# on send - timer expiry
# 	start_timer
# on fail
# 	stp_retransmit

# TEST PRINT CODE
#file = sys.argv[1]
#x = Sender('127.0.0.1',4096,file,0,0,0,0,0)	# create instance of sender
#packet = x.read_file()			# open file, create segment
#x.stp_send(packet)				# send segment

###################
# MAIN FUNCTION???
###################

num_args = 9
if len(sys.argv) != num_args:				# check num args
	print("Usage: ./Receiver.py host_ip port file.txt MWS MSS timeout pdrop seed")
else:
	r_host_ip, r_port, file, MWS, MSS, timeout, pdrop, seed  = sys.argv[1:]		# grab args
	sender = Sender(r_host_ip, r_port, file, MWS, MSS, timeout, pdrop, seed) # create instance of sender
	print("Sender is ready ...")
	log = open("Sender_log.txt","w")		# create log for recording segment info

	data = sender.stp_send()		# app passes data down to sender transport layer
	packet = sender.make_pkt(data)			# create packet from data
	sender.udp_send(packet)			# send packet over UDP

	sender.stp_close()					# everything done -> close connection



'''
	def udp_send(receiver_host_ip, receiver_port)

	while True:
		#if (data received from app layer):
			stp_packet = STPPacket(data, 0, 0, True, False, False)
			# if (timer not started):
			#		start_timer()
			socket = socket(AF_INET, SOCK_DGRAM)
			NextSeqNum = NextSeqNum + length(data)
		#elif (timeout):
		# ACK received, with valid ACK field value = y
		# sendBase = seq numebr of oldest unacknowledged byte
		#else:
'''









################################
# DATA RECEIVED FROM APP LAYER
################################

# Sender waits for data to be passed down from app layer
# wait()

# stp_send(data) is called by app layer.
# stp_send(data)

# send packet via. udp_send
# -> sender reads file + creates STP Segment (seq num + packet sndpkt + checksum)
# -> create and transmit UDP datagram + UDP send
# -> start timer (if another time is not already running from another segment)
#    timer is associated the oldest unacknowledged segment
# sndpkt = make_pkt(0, data, checksum)
# udt_send(sendpkt)
# start_timer

##########################
# WAIT FOR RESPONSE - NAK
##########################

# if waiting, can't receive more data from app layer = stp_send() can't occur

# ACK response packet comes back
# stp_rcv(rcvpkt) && isACK

# NAK response packet comes back
# stp_rcv(rcvpkt) && isNAK
# retransmit


##########################
# WAIT FOR RESPONSE - NAK
##########################




