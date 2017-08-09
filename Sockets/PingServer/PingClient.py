# PING CLIENT PROGRAM
#
# This is a client-side program makes ping requests
# to the server.

import sys

total = len(sys.argv)
cmdargs = str(sys.argv)

from socket import *
from time import sleep
import datetime

serverName = '127.0.0.1'
serverPort = 12000 # change port number if required

clientSocket = socket(AF_INET, SOCK_DGRAM)

while 1:
	sequenceNum = str(0)
	timeStamp = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
	ping = 'PING ' + sequenceNum + timeStamp
	print ping
	clientSocket.sendto(ping, (serverName, serverPort))			# transmits data to server
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)	# receives data from server


print 'From Server:', modifiedMessage
clientSocket.close()















