#!/usr/bin/python

# Simple Transport Protocol (STP)
# Sender side program
#
# Author: Brian Lam

import pickle
import sys
import time
from random import *
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

class PLD:
	def __init__(self, pdrop):
		self.pdrop = pdrop

	def exe_pld(self):
		rand = random()
		rand = str(rand)
		if rand > self.pdrop:
			return True
		else:
			return False

class Sender:

	# initialise sender data
	def __init__(self, r_host_ip, r_port, file, MWS, MSS, timeout, pdrop, seed):
		self.r_host_ip = r_host_ip
		self.r_port = int(r_port)
		self.file = file      		# grab file from arg[4]
		self.MWS = int(MWS)			# max window size
		self.MSS = int(MSS) 		# max segment size
		self.timout = timeout
		self.pdrop = pdrop
		self.seed = int(seed)

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
		SYN = STPPacket('', seq_num, ack_num, ack=False, syn=True, fin=False)
		return SYN

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
	def udp_send(self, stp_packet):
		self.socket.sendto(pickle.dumps(stp_packet), (self.r_host_ip, self.r_port))

	# FIN close
	def stp_close(self):
		self.socket.close()

	# retransmit
	def retransmit(self, packet):
		self.socket.sendto(pickle.dumps(packet), (self.r_host_ip, self.r_port))
		sender.update_log("snd", 'D', packet)

	# Update Sender_log.txt
	def update_log(self, action, pkt_type, packet):
		print("Updating sender log . . .")
		# grabbing header fields
		seq = packet.seq_num
		ack = packet.ack_num
		size = len(packet.data)
		# clocking time
		curr_time = time.clock()
		curr_time = curr_time * 1000
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
		f = open("Sender_log.txt", "a+")
		f.write(final_str)
		f.close()

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

	#def check_time(self):
	#	curr_time = time.clock()
	#	curr_time = curr_time * 1000


### CHECK CORRECT USAGE ###
num_args = 9
if len(sys.argv) != num_args:
	print("Usage: ./Receiver.py host_ip port file.txt MWS MSS timeout pdrop seed")
else:
	### SET UP VARIABLES ###
	# init seq/ack vars
	seq_num = 0
	ack_num = 0
	sendbase = 0 	# oldest un_ACK seg's first byte
	num_unacked = 0 # tracking remaining unack'd segs
	# sender states
	state_closed = True
	state_syn_sent = False
	state_timeout = False
	state_established = False # send segment
	state_end = False
	# track states and packets
	prev_state = None
	curr_packet = None
	prev_pkt = None
	# track packet progress
	num_transmitted = 0
	num_retransmitted = 0
	num_dropped = 0
	# grab args
	r_host_ip, r_port, file, MWS, MSS, timeout, pdrop, seed = sys.argv[1:]
	# timing vars
	curr_time = 0
	prev_time = 0
	timeout = timeout
	# reset sender_log.txt
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

	# Create PLD
	pld = PLD(pdrop)

	### MAIN LOOP EVENT ###
	while True:
		print("start of loop")

		### CLOSED STATE ###
		# send SYN seg
		if state_closed == True:
			print("\n===================== STATE: CLOSED")
			syn_pkt = sender.make_SYN(seq_num, ack_num)
			sender.udp_send(syn_pkt)
			sender.update_log("snd", 'S', syn_pkt)
			state_closed = False
			state_syn_sent = True

		### SYN SENT STATE - WAIT FOR SYNACK ###
		# wait for SYNACK seg
		if state_syn_sent == True:
			print("\n===================== STATE: SYN SENT")
			synack_pkt = sender.stp_rcv()
			# check if SYNACK
			if synack_pkt.ack == True and synack_pkt.syn == True:
				# acknowledge SYNACK, update log
				ack_num = synack_pkt.seq_num + 1
				sender.update_log("rcv", 'SA', synack_pkt)
				# send ACK
				seq_num += 1
				ack_pkt = sender.make_ACK(seq_num, ack_num)
				sender.udp_send(ack_pkt)
				sender.update_log("snd", 'A', ack_pkt)
				print("SYNACK received . . .")
				# 3-way-handshake complete
				state_established = True
				state_syn_sent = False

		### ESTABLISHED STATE ###
		# send payload segments to receiver until whole file transferred
		if state_established == True:
			print("\n===================== STATE: CONNECTION ESTABLISHED")
			# grab MSS data, then create packet
			payload = sender.split_data(app_data, data_progress)
			packet = STPPacket(payload, seq_num, ack_num, ack=False, syn=False, fin=False)
			# time between last packet and this packet
			curr_time = time.clock() * 1000
			time_diff = curr_time - prev_time
			print("CURR TIME = {}").format(curr_time)
			print("PREV TIME = {}").format(prev_time)
			print("TIME DIFF = {}").format(time_diff)
			print("TIMEOUT = {}").format(timeout)
			# prev packet exists, timeout reached -> retransmit
			if prev_pkt != None and time_diff > timeout:
				print("PACKET RETRANSMITTING")
				prev_pkt = packet
				sender.retransmit(packet); num_unacked += 1
				seq_num += len(payload)
				num_retransmitted += 1
				prev_pkt = None
				continue
			# pass packet through PLD
			result = pld.exe_pld()
			if result == True:
				print("PACKET SENT SUCCESSFULLY")
				sender.udp_send(packet); num_unacked += 1
				seq_num += len(payload)
				sender.update_log("snd", 'D', packet)
				num_transmitted += 1
			else:
				prev_time = time.clock() * 1000
				print("PACKET DROPPED")
				num_dropped += 1
				sender.update_log("drop", 'D', packet)
				sender.retransmit(packet); num_unacked += 1
				seq_num += len(payload)
				num_retransmitted += 1
			# TIMER = tracking the oldest unacknowledged segment
			if curr_time == 0:
				curr_time = time.clock() * 1000
				print("<<< TIMER STARTED = {} >>>".format(curr_time))
			# update data progress and seq_num
			data_progress += len(payload)
			# wait for RCV ack
			print("\n==== STATE: WAITING FOR ACK ===")
			ack_pkt = sender.stp_rcv()
			sender.update_log("rcv", 'A', ack_pkt)
			ack_num += len(ack_pkt.data)
			if state_end != True and ack_pkt.ack == True and ack_pkt.ack_num > sendbase:
				print("<<< ACK RECEIVED >>>")
				num_unacked -= 1
				sendbase = ack_pkt.ack_num
				if num_unacked == 0:
					curr_time = time.clock() * 1000
			# whole file has been sent, begin close connection
			if data_progress == data_len:
				# send FIN
				fin_pkt = sender.make_FIN(seq_num, ack_num)
				sender.udp_send(fin_pkt)
				sender.update_log("snd", 'F', fin_pkt)
				state_end = True
				state_established = False

		### END OF CONNECTION ###
		# wait for ACK
		if state_end == True:
			print("\n=== STATE: END OF CONNECTION ===")
			ack_pkt = sender.stp_rcv() # ACK log combined with FIN below
			print("ACK IS: {}".format(ack_pkt.ack_num))
			print("SEQ IS: {}".format(ack_pkt.seq_num))
			# received ACK -> wait for FIN
			if ack_pkt.ack == True:
				fin_pkt = sender.stp_rcv()
				print("ACK IS: {}".format(fin_pkt.ack_num))
				print("SEQ IS: {}".format(fin_pkt.seq_num))
				sender.update_log("rcv", 'FA', fin_pkt)
				# received FIN -> send ACK + wait 30 seconds
				if fin_pkt.fin == True:
					# acknowledge FINACK
					ack_num += 1
					# send ACK
					ack_pkt = sender.make_ACK(seq_num, ack_num)
					sender.udp_send(ack_pkt)
					sender.update_log("snd", 'A', ack_pkt)
					print("Waiting 30 seconds")
					#time.sleep(30)
					break

	sender.stp_close()
	# print out complete log
	print("\n### FINAL SENDER LOG ###")
	f = open("Sender_log.txt", "a+")
	data = "Data Transferred = {} bytes\n".format(data_len)
	seg_sent = "Segments Sent = {}\n".format(num_transmitted)
	pkt_dropped = "Packets Dropped = {}\n".format(num_dropped)
	pkt_delayed = "Packets Delayed = N/A\n"
	seg_retrans = "Segments Retrans = {}\n".format(num_retransmitted)
	ack_duplicate = "Duplicate Acks = N/A"
	final_str = "\n" + data + seg_sent + pkt_dropped + pkt_delayed + seg_retrans + ack_duplicate
	f.write(final_str)
	f.close()
	f = open("Sender_log.txt", "r")
	print(f.read())
	f.close()

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




