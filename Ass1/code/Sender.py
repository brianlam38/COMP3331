#!/usr/bin/python3

# Simple Transport Protocol (STP)
#
# Sender side program
# 
# Three major components to data transmission and re-transmission:
# 1. Data received from app layer above
# 2. Timer timeout
# 3. ACK receipt

import pickle
import argv
from socket import *

# exe format:
# python sender.py receiver_host_ip receiver_port file.txt MWS MSS timeout pdrop seed

class STPPacket:
	def __init_(self, data, seq_num, ack_num, ack=False, syn=False, fin=False)
		self.data = data
		self.seq_num = seq_num
		self.ack_num = akc_num
		self.ack = ack
		self.syn = syn
		self.fin = fin


class Sender:
	# you need to create this.
	# a lot more complicated, but just follow the assignment spec
	# you can do go-back-N, selective repeat, whatever works
	# also need sequence number

	# missing: MWS, pdrop, seed

	# initialise sender data: seq number, timeout
	def __init_(self, init_seq_num, timeout)
		self.init_seq_num = 0
		self.timeout = 0

	# read file from input -> separate into segments -> pop into stack
	# NOTE: max_seg_size = max bytes carried in each STP segment
	#       
	def read_file(file, max_seg_size)
		file = argv[4]				# grab file from args
		file_size = len(file) 		# determine filesize
		# read file
		# segment = filesize / max_seg_size

	def udp_send(receiver_host_ip, receiver_port)


	# NextSeqNum = InitialSeqNumber
	# SendBase = InitialSeqNumber

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






# how to create packet?
# myPacket = Packet(data, 0, 0, True, False, False)

# Packet is an object. How to send and receive this over UDP?

# send
import pickle
stp_packet = STPPacket(data, . . .)
socket.sendto(pickle.dumps(stp_packet), (client_ip, client_port))

# on send - timer expiry
start_timer

# on fail
stp_retransmit



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







