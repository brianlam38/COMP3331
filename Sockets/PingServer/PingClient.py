# PING CLIENT PROGRAM
#
# This is a client-side program makes ping requests to the server.

import sys

total = len(sys.argv)
cmdargs = str(sys.argv)

from socket import *
import time

server_name = '127.0.0.1'
server_port = 12000 # change port number if required
client_socket = socket(AF_INET, SOCK_DGRAM)

seq_num = 0
while seq_num < 10:
	send_time = time.time()									# transmit time
	ping = 'Ping to ' + server_name + ', seq = ' + str(seq_num) + ', '  + str(send_time)
	client_socket.sendto(ping, (server_name, server_port))	# transmit data to server
	time.sleep(1)											# wait 1
										
	reply, server_address = client_socket.recvfrom(2048)	# receive data from server
	recv_time = time.time()									# receive time

	RTT = round(recv_time - send_time, 3)					# calculate RTT
	print 'From server: ', reply
	seq_num += 1

client_socket.close()

