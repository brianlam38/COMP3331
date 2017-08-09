"""
# TCP Server Program

from socket import *

serverPort = 12000 # change port number if required
serverSocket = socket(AF_INET, SOCK_STREAM)				# create socket for client
serverSocket.bind(('', serverPort))						# binds address (hostname, port numer) to socket
serverSocket.listen(1)									# Listen / wait for connections made to the socket
print "The server is ready to receive"						# Arg = max no. of queued connections

while 1:
    connectionSocket, addr = serverSocket.accept()		# passively accepts TCP client connection
    														# Waiting until connection arrives
    														# New socket created on return
    sentence = connectionSocket.recv(1024)				# receives data from client

    capitalizedSentence = sentence.upper()				# manipulates data

    connectionSocket.send(capitalizedSentence)			# transmits data to client
    connectionSocket.close()							# close the socket

"""

# UDP server program

from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print "The server is ready to receive"

while 1:
	message, clientAddress = serverSocket.recvFrom(2048)
	modifiedMessage = message.upper()
	serverSocket.sendto(modifiedMessage, clientAddress)






