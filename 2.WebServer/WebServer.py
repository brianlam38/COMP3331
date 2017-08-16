#!/usr/bin/python

# SIMPLE WEB SERVER
#
# Author: Brian Lam
# Course: COMP3331 Networks

# STEPS
# 1. Create connection socket when contacted by a client (browser)
# 2. Receive HTTP request from this connection.
#    Process the GET request (assume only GET requests are received)
# 3. Parse the request to determine the specific file being requested
# 4. Get the requested file from the server's file system
# 5. Create a HTTP response message consisting of the requested file preceded by header lines
# 6. Send the response over the TCP connection to the requesting browser
# 7. If the requested file is not present on the server, send a HTTP "404 not found" message to client

from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)				# create socket for client
serverSocket.bind(('', serverPort))						# binds address (hostname, port numer) to socket
serverSocket.listen(1)									# Listen / wait for connections made to the socket
print "The server is ready to receive\n"				#		Arg 1 = max no. queued connections

while 1:
	print "Ready to serve"
	connectionSocket, addr = serverSocket.accept()		# passively accepts TCP client connection
																# Waiting until connection arrives
																# New socket created on return
	# Receive and send client requests
	try:
		request = connectionSocket.recv(1024)				# receives get request from client

		message = request.split()[1];						# parse get request
		file_name = message.replace('/', '')					# remove slash
		print file_name, '\n\n'								

		file = open(file_name)								# get the requested file from file system
		connectionSocket.send('\nHTTP/1.1 200 OK\n\n')		# send header line
		connectionSocket.send(file.read())					# send HTTP response message to client
	# IO Exception
	except Exception:
		connectionSocket, addr = serverSocket.accept()
		connectionSocket.send('404 not found')

connectionSocket.close()									# close the socket










