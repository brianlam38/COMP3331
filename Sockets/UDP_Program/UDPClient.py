# UDP CLIENT PROGRAM
#
# This is a client-side program for making ping requests to a server
#
# UDP CLIENT PROGRAM
#
# This is the client-side program to
# send requests to the server.

import sys

total = len(sys.argv)
cmdargs = str(sys.argv)

from socket import *

serverName = '127.0.0.1'
serverPort = 12000 # change port number if required

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = raw_input('Input sentence:')

clientSocket.sendto(message, (serverName, serverPort))		# transmits data to server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)	# receives data from server
print 'From Server:', modifiedMessage
clientSocket.close()















