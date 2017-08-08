import sys
total = len(sys.argv)
cmdargs = str(sys.argv)

from socket import *
serverName = str(sys.argv[1]);
serverPort = 12000 #change this port number if required
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
clientSocket.close()
