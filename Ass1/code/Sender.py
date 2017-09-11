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
	# a lot more complicated, but just follow the assignment spec
	# you can do go-back-N, selective repeat, whatever works
	# also need sequence number

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

	socket = socket(AF_INET, SOCK_DGRAM)
	#socket.setblocking(0)	# temp fix
	#socket.settimeout(100)	# temp fix

	# Read file from input, extract data and store in class
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

	# creating packet to send to receiver
	# modify later to create packet based off MSS / MWS
	# -> separate into segments -> pop into stack
	# SENDER SYN + PAYLOAD

	# send via. UDP to receiver
	def udp_send(self, stp_packet):
		# sender explicitly attaches IP destination address and port no. to each packet
		self.socket.sendto(pickle.dumps(stp_packet), (self.r_host_ip, self.r_port))
		#return_msg, server_add = socket.recvfrom(2048)	# receives data from server

	# receive packet from receiver
	# convert packet to dict format
	def stp_rcv(self):
		data, addr = self.socket.recvfrom(2048)   # extracts sender IP and port number
		stp_packet = pickle.loads(data)			  # converts data back to packet
		return stp_packet

	# FIN close
	def stp_close(self):
		self.socket.close()

	# Determine state - for timeout
	#def determine_state(self, state):
	#	if state = 'state_closed':
	#
	#	return state


###################
# MAIN FUNCTION???
###################

###################
#NOTE : CONTROL PACKETS ARE LOSSLESS, REMOVE TIMEOUTS FROM THESE CASES
###################

### CHECK CORRECT USAGE ###
num_args = 9
if len(sys.argv) != num_args:
	print("Usage: ./Receiver.py host_ip port file.txt MWS MSS timeout pdrop seed")
else:
	### SET UP VARIABLES ###
	# initial seq ack numbers
	seq_num = 0
	ack_num = 0
	# sender states
	state_closed = True
	state_syn_sent = False
	state_timeout = False
	state_established = False
	# track states and packets
	prev_state = None
	curr_packet = None
	# grab args, create Sender_log.txt
	r_host_ip, r_port, file, MWS, MSS, timeout, pdrop, seed = sys.argv[1:]
	log = open("Sender_log.txt","w")

	# App layer initiates client TCP
	print("Sender initiated . . . creating socket object")
	sender = Sender(r_host_ip, r_port, file, MWS, MSS, timeout, pdrop, seed)
	
	# loop until connection closed						
	while True:
		print("looping")
	### CLOSED STATE ###
		if state_closed == True:
			prev_state = 'state_closed'
			print("STATE: CLOSED")

			syn_pkt = STPPacket(None, seq_num, ack_num, ack=False, syn=True, fin=False)	# create SYN packet
			curr_packet = syn_pkt 			# set curr pkt = SYN
			sender.udp_send(syn_pkt)		# send SYN -> receiver
			state_closed = False
			state_syn_sent = True

	### SYN SENT STATE - WAIT FOR SYNACK ###
		if state_syn_sent == True:
			prev_state = 'state_syn_sent'
			print("STATE: SYN SENT")
			synack_pkt = sender.stp_rcv()
			print("synack ack_num = {}".format(synack_pkt.ack_num))
			print("synack syn = {}".format(synack_pkt.syn))
			# correct synack segment
			if synack_pkt.ack_num == 0 and synack_pkt.syn == True:
				print("SYNACK received . . .")
				state_established = True
			# timeout
			#elif time == timeout
			#	print("SYNACK timeout . . .")
			#	state_timeout = True
			#	state_syn_sent = False

	### TIMEOUT / RESEND STATE - only needs to care about established state ###
		if state_timeout == True:
			print("STATE: RESEND PACKET")
			packet = curr_packet
			state = prev_state
			sender.udp_send(packet)
			state_timeout = False
			state_syn_sent = True

	### ESTABLISHED STATE - SYNACK RECEIVED, BEGIN PAYLOAD SEND ###
		if state_established == True:
			print("STATE: Established connection . . .")
			data = sender.stp_send()		# grab app-layer payload
			packet = STPPacket(data, 0, 0, ack=False, syn=False, fin=False)		# create packet from data
			#sender.udp_send(packet)											# send packet over UDP
			sender.stp_close()												# everything done -> close connection
			break


		# elif timer = timeout, resend packet
		#		syn_pkt = sender.make_pkt(None, seq_num, ack_num, ack=False, syn=True, fin=False)
		#		sender.udp_send(syn_pkt)

		# BUFFER = ONLY HAPPENS ON RECEIVER SIDE
		# else
		#		put in buffer
		#		continue


# on send - timer expiry
# 	start_timer
# on fail
# 	stp_retransmit


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




