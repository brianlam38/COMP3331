# PING SERVER PROGRAM

from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"

while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.upper()
	# UDP has no "connection socket" between client / server
	# sender explicitly attaches IP destination address and port no. to each packet
	# receiver extracts sender IP address and port no. from received packet
	serverSocket.sendto(modifiedMessage, clientAddress)






