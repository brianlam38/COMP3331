from socket import *
serverPort = 12000 # change port number if required
serverSocket = socket(AF_INET, SOCK_STREAM)				# create socket for client
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print "The server is ready to receive"
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)				# receive TCP message
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()

