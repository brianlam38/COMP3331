"""
# TCP CLIENT PROGRAM

import sys

total = len(sys.argv)
cmdargs = str(sys.argv)

from socket import *

serverName = str(sys.argv[1]);						# Briandawgg.local
serverPort = 12000 #change port number if required
clientSocket = socket(AF_INET, SOCK_STREAM)			# create socket for server
														# AF_INET = ip address family (e.g. Internet Protocol v4 addresses)
														# SOCK_STREAM = TCP socket (SOCK_DGRAM = UDP socket)
clientSocket.connect((serverName, serverPort))		# initiates a TCP server connection

sentence = raw_input('Input lowercase sentence:')	# grab client input

clientSocket.send(sentence)							# transmits data to server
modifiedSentence = clientSocket.recv(1024)			# receives data from server
print 'From Server:', modifiedSentence
clientSocket.close()								# close the socket
"""

# UDP CLIENT PROGRAM

from socket import *

serverName = 'hostname'
serverPort = 12000 # change port number if required

clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)
message = raw_input('Input sentence:')

clientSocket.send(sentence)							# transmits data to server
modifiedSentence = clientSocket.recv(1024)			# receives data from server
print 'From Server:', modifiedSentence
clientSocket.close()















