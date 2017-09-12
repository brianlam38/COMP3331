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
		self.MWS = int(MWS)			# max window size
		self.MSS = int(MSS) 		# max segment size
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

	# Update Sender_log.txt
	def update_log(self, action, pkt_type, seq, size, ack):
		print("Updating sender log . . .")
		curr_time = time.clock() 	 # temp timer
		curr_time = curr_time * 1000 # convert to MS
		curr_time = str(curr_time); seq = str(seq); size = str(size); ack = str(ack)
		# init arrays of args and col lens
		col_lens = [5, 7, 4, 4, 3, 3]
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
		f = open("Sender_log.txt", "a+")
		f.write(final_str)
		f.close()

	#def start_timer(self):
		# do stuff

	def split_data(self, app_data, start):
		length = len(app_data)
		# calculate start : end range
		end = data_progress + self.MSS
		# not exceeding total size
		if end < length:
			payload = app_data[start:end]
		# exceeding total size
		else:
			payload = app_data[start:length]
		return payload


###################
#NOTE : CONTROL PACKETS ARE LOSSLESS, REMOVE TIMEOUTS FROM THESE CASES
###################

#i wrote an update_log function that takes in the action/type as arguments
#and called it everywhere, maybe that might be usefvul for you too

### CHECK CORRECT USAGE ###
num_args = 9
if len(sys.argv) != num_args:
	print("Usage: ./Receiver.py host_ip port file.txt MWS MSS timeout pdrop seed")
else:
	### SET UP VARIABLES ###
	# timing vars
	timer = 0
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
	state_end = False
	# track states and packets
	prev_state = None
	curr_packet = None
	# grab args, reset sender_log.txt
	r_host_ip, r_port, file, MWS, MSS, timeout, pdrop, seed = sys.argv[1:]
	f = open("Sender_log.txt","w")
	f.close()

	# App layer initiates, create socket, store app-layer file
	print("Sender initiated . . .")
	sender = Sender(r_host_ip, r_port, file, MWS, MSS, timeout, pdrop, seed)
	app_data = sender.stp_send()

	# track progress of file sent
	data_progress = 0
	data_len = len(app_data)
	print("LEN OF DATA = {}".format(data_len))

	### MAIN LOOP EVENT ###
	while True:
		print("start of loop")

		### CLOSED STATE ###
		# send SYN seg
		if state_closed == True:
			print("\n===================== STATE: CLOSED")
			syn_pkt = sender.make_SYN(seq_num, ack_num)
			sender.udp_send(syn_pkt); print("Sending SYN")
			sender.update_log("snd", 'S', 0, 0, 0)
			state_closed = False
			state_syn_sent = True

		### SYN SENT STATE - WAIT FOR SYNACK ###
		# wait for SYNACK seg
		if state_syn_sent == True:
			print("\n===================== STATE: SYN SENT")
			synack_pkt = sender.stp_rcv()
			sender.update_log("rcv", 'SA', 0, 0, 0)
			print("synack data = {}".format(synack_pkt.data))
			print("synack ack = {}".format(synack_pkt.ack))
			print("synack syn = {}".format(synack_pkt.syn))
			# received SYNACK -> send ACK -> 3-way-handshake complete
			if synack_pkt.ack == True and synack_pkt.syn == True:
				ack_pkt = sender.make_ACK(seq_num, ack_num)
				sender.udp_send(ack_pkt); print("Sending ACK")
				sender.update_log("snd", 'A', 0, 0, 0)
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
			print("\n===================== STATE: RESEND PACKET")
			packet = curr_packet
			state = prev_state
			sender.udp_send(packet)
			state_timeout = False
			state_established = True

		### ESTABLISHED STATE ###
		# send payload segments to receiver until whole file transferred
		if state_established == True:
			print("\n===================== STATE: CONNECTION ESTABLISHED")
			# manipulate app_data to create separate packets
			payload = sender.split_data(app_data, data_progress)
			# manipulate app_data to create separate packets
			packet = STPPacket(payload, 0, 0, ack=False, syn=False, fin=False)
			sender.udp_send(packet); print("Sending payload packet")
			sender.update_log("snd", 'D', 0, 0, 0)
			data_progress += len(payload)
			# whole file has been sent, begin close connection
			if data_progress == data_len:
				# send FIN
				fin_pkt = sender.make_FIN(seq_num, ack_num)
				sender.udp_send(fin_pkt); print("Sending FIN")
				sender.update_log("snd", 'F', 0, 0, 0)
				state_end = True
				state_established = False

		### END OF CONNECTION ###
		# wait for ACK
		if state_end == True:
			print("\n=== STATE: END OF CONNECTION ===")
			ack_pkt = sender.stp_rcv() # ACK log combined with FIN below
			# received ACK -> wait for FIN
			if ack_pkt.ack == True:
				fin_pkt = sender.stp_rcv()
				sender.update_log("rcv", 'FA', 0, 0, 0)
				# received FIN -> send ACK + wait 30 seconds
				if fin_pkt.fin == True:
					ack_pkt = sender.make_ACK(seq_num, ack_num)
					sender.udp_send(ack_pkt)
					sender.update_log("snd", 'A', 0, 0, 0)
					print("Waiting 30 seconds")
					#time.sleep(30)
					break

	sender.stp_close()
	# print out complete log
	print("\n### FINAL SENDER LOG ###")
	f = open("Sender_log.txt", "r")
	print(f.read())


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




