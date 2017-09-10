#!/usr/bin/python

# Simple Transport Protocol (STP)
#
# Receiving side program

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
	# you need to create this
	# receiver needs to have a sequence number so it can deal with out-of-order pakes
	# receiver receives stp_packet and then writes the data inside the packet

	port = 4096
	socket = socket(AF_INET, SOCK_DGRAM)
	socket.bind(('', port))
	print("The server is ready to receive")

	while 1:
		data, addr = socket.recvfrom(2048)   # extracts sender IP and port number
		stp_packet = pickle.loads(data)
		print(data)
		socket.sendto(data, addr)


	#def stp_rcv(self, packet):
	#	print("data received")


	#def stp_rcv(self, packet)


	# receive packet
	#data, addr = socket.recvfrom(4096)
	#stp_packet = pickle.loads(data)


x = Receiver()
#x.stp_rcv()



# after receiving packet
#received_seq_num = stp_packet.seq_num

# on receive
# The receiver should generate ACK immediately after receiving a data segment
#self.timer.cancel()

'''
The receiver is expected to buffer out-of-order arrival packets.
 The receiver should first open a UDP listening socket on receiver_port and then wait for segments to arrive from the Sender.
 The first segment to be sent by the Sender is a SYN segment and the receiver is expected to reply a SYNACK segment.
 After the completion of the three-way handshake, the receiver should create a new text file called file.txt.
 All incoming data should be stored in this file.
 The Receiver should first extract the STP packet from the arriving UDP datagrams and then extract the data (i.e. payload) from the STP packet.
 Note that, the Receiver is allowed to examine the header of the UDP datagram that encapsulates the STP Packet to determine the UDP port and IP address that the Sender is using.
 The data should be written into file.txt.
At the end of the transfer, the Receiver should have a duplicate of the text file sent by the Sender.
 You can verify this by using the diff command on a Linux machine (diff file1.txt file2.txt).
 The Receiver should also maintain a log file titled Receiver_log.txt where it records the information about each segment that it sends and receives.
 The format should be exactly similar to the sender log file as outlined in the Sender specification.
The Receiver should terminate after the connection closure procedure initiated by the sender concludes.
The Receiver should also print the following statistics at the end of the log file (i.e. Receiver_log.txt):
'''


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




