#!/usr/bin/python

# Simple Transport Protocol (STP)
# Sender side program
#
# Author: Brian Lam

import pickle
import sys
import time
from socket import *

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

	# initialise sender data
	def __init__(self, r_host_ip, r_port, file, MWS, MSS, timeout, pdrop, seed):
		self.r_host_ip = r_host_ip
		self.r_port = int(r_port)
		self.file = file      		# grab file from arg[4]
		self.MWS = MWS				# max window size
		self.MSS = MSS 				# max segment size
		self.timout = timeout
		self.pdrop = pdrop
		self.seed = seed

	# create UDP socket
	socket = socket(AF_INET, SOCK_DGRAM)

	# Read file from input, extract data and store in class
	# NOTE: max_seg_size = max bytes carried in each STP segment

	# App-layer passing down data
	def stp_send(self):
		#file_size = len(self.file) 		# file_size = os.path.getsize(file)
		#print(file_size)
		# read file
		# segment = filesize / max_seg_size
		# seg_size

		# preparing data
		f = open(self.file, "r")	# open file
		data = f.read()				# read file + store in data obj
		return data

	# receive packet from server, return packet
	def stp_rcv(self):
		data, addr = self.socket.recvfrom(2048)
		stp_packet = pickle.loads(data)
		return stp_packet

	# create SYN
	def make_SYN(self, seq_num, ack_num):
		print("Creating SYN")
		SYN = STPPacket('SYN', seq_num, ack_num, ack=False, syn=True, fin=False)
		return SYN

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
	def udp_send(self, stp_packet):
		self.socket.sendto(pickle.dumps(stp_packet), (self.r_host_ip, self.r_port))

	# FIN close
	def stp_close(self):
		self.socket.close()

###################
#NOTE : CONTROL PACKETS ARE LOSSLESS, REMOVE TIMEOUTS FROM THESE CASES
###################

### CHECK CORRECT USAGE ###
num_args = 9
if len(sys.argv) != num_args:
	print("Usage: ./Receiver.py host_ip port file.txt MWS MSS timeout pdrop seed")
else:
	### SET UP VARIABLES ###
	# init seq/ack vars
	seq_num = 0
	ack_num = 0
	next_seq_num = 0
	next_ack_num = 0
	# sender states
	state_closed = True
	state_syn_sent = False
	state_timeout = False
	state_established = False
	# track states and packets
	prev_state = None
	curr_packet = None
	# track progress of file sent
	app_data_progress = 0
	# grab args, create log.txt
	r_host_ip, r_port, file, MWS, MSS, timeout, pdrop, seed = sys.argv[1:]
	log = open("Sender_log.txt","w")

	# App layer initiates, create socket, store app-layer file
	print("Sender initiated . . .")
	sender = Sender(r_host_ip, r_port, file, MWS, MSS, timeout, pdrop, seed)
	app_data = sender.stp_send()

	### MAIN LOOP EVENT ###
	while True:
		print("start of loop")

		### CLOSED STATE ###
		# send SYN seg
		if state_closed == True:
			print("===================== STATE: CLOSED")
			syn_pkt = sender.make_SYN(seq_num, ack_num)
			sender.udp_send(syn_pkt); print("Sending SYN")
			state_closed = False
			state_syn_sent = True

		### SYN SENT STATE - WAIT FOR SYNACK ###
		# wait for SYNACK seg
		if state_syn_sent == True:
			print("===================== STATE: SYN SENT")
			synack_pkt = sender.stp_rcv()
			print("synack data = {}".format(synack_pkt.data))
			print("synack ack = {}".format(synack_pkt.ack))
			print("synack syn = {}".format(synack_pkt.syn))
			# received SYNACK -> send ACK -> 3-way-handshake complete
			if synack_pkt.ack == True and synack_pkt.syn == True:
				ack_pkt = sender.make_ACK(seq_num, ack_num)
				sender.udp_send(ack_pkt); print("Sending ACK")
				print("SYNACK received . . .")
				state_established = True
				state_syn_sent = False
			# timeout
			#elif time == timeout
			#	print("SYNACK timeout . . .")
			#	state_timeout = True
			#	state_syn_sent = False

		### TIMEOUT / RESEND STATE ###
		if state_timeout == True:
			print("===================== STATE: RESEND PACKET")
			packet = curr_packet
			state = prev_state
			sender.udp_send(packet)
			state_timeout = False
			state_established = True

		### ESTABLISHED STATE ###
		if state_established == True:
			print("===================== STATE: CONNECTION ESTABLISHED")
			# manipulate app_data to create separate packets
			# manipulate app_data to create separate packets
			# manipulate app_data to create separate packets
			packet = STPPacket(app_data, 0, 0, ack=False, syn=False, fin=False)
			sender.udp_send(packet); print("Sending payload packet")
			app_data_progress += len(app_data)
			# whole file has been sent, begin close connection
			if app_data_progress == len(app_data):
				# send FIN
				fin_pkt = sender.make_FIN(seq_num, ack_num)
				sender.udp_send(fin_pkt); print("Sending FIN")
				state_end = True
				state_established = False

		### END OF CONNECTION ###
		# wait for ACK
		if state_end == True:
			print("=== STATE: END OF CONNECTION ===")
			ack_pkt = sender.stp_rcv()
			# received ACK -> wait for FIN
			if ack_pkt.ack == True:
				fin_pkt = sender.stp_rcv()
				# received FIN -> send ACK + wait 30 seconds
				if fin_pkt.fin == True:
					ack_pkt = sender.make_ACK(seq_num, ack_num)
					sender.udp_send(ack_pkt)
					print("Waiting 30 seconds")
					#time.sleep(30)
					break

	sender.stp_close()


	### TIMEOUT ###
	#while True:
	#	try:
	#		print("waiting . . .")
	#		sender.socket.settimeout(2)
	#	except timeout:
	#		print("Connection closed")
	#		break
	#break

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




