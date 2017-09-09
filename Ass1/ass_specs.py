# NOTES FOR ASSIGMENT 1

Implement a reliable transport protocol over UDP. -> Simple Transport Protocol 'STP'

1. Implement the file transfer using the simpler alternating-bit (stop-and-wait) protocol
   (version rdt3.0 from the textbook).
2. Make sure that your program works without implementing the PLD module.
3. Implement the packet drop functionality of the PLD and test your protocol.
4. Extend your code to handle transmission of a window of packets (i.e., MWS).
5. Send a window of packets and wait for all acknowledgements to come back before
   sending another window worth of data.
6. As before, test the no loss case first.
7. Extend your program to handle packet losses.
8. Once you have the complete STP protocol implemented run comprehensive tests.

--------

Basic setup of the assignment:
-> File is to be transferred from the Sender to the Receiver.
-> Sender will run on the sender-side while Receiver runs on the receiver-side.
-> Note: data segments will flow from the sender to the receiver, while ACK segments will flow
   from the receiver to the sender.

TWO VERSIONS: Standard + Extended

-------

1. Before you start your implementation, make sure you read the Spec very CAREFULLY.

2. Make sure you properly defined a data structure to represent a TCP segment,
which should at have a 'header portion' + 'payload portion'. 
-> The header defines the type of the segment (wether it is a 'data packet' or a 'control packet').
For example, if you want to send a SYN packet to the server, do not try
to send a plain text "SYN". Think about if we ask you to send a text file,
whose content is just one word "SYN". Then your program will not accept it as a data.

----------------

You dont need to modify anything in the socket DGRAM.
First define a data structure like this:

TCDSeg {
	int type // 0-data, 1-ack, 2-SYN, 3-SYNACK
	.....
	String data
}

When you want to send a piece of data, say "hello", then create a TCPSeg instance:

TCPSeg.type = 0;
TCPSeg.data = "hello";

Then send the instance to the server.
The server upon reception, it first check the type filed,
finds that it is a data packet, then put the received string into the buffer.

If you want to send a SYN to the server. 
TCP.Seg.type=2;
TCPSeg.data = " ";
Same, send the structure to the server,
the server then knows it is a SYN packet by checking the type field.

I think Python socket can pass data structure

--------

3.1 File Names = sender.py | receiver.py

3.1 List of Features by Sender and Receiver:

	[1] Three way handshake 'SYN, SYN+ACK, ACK' for the connection establishment
	- ACK sent by the sender to conclude handshake should not contain payload / data

	[2] Four-segment connection termination 'FIN, ACK, FIN, ACK'
	- Sender will initiate connection close once entire file is transmitted
	- Refer to 3.5.6

	[3] Sender must maintain single-timer for timeout operation
	- Refer to 3.5.4

	[4] Sender should implement all features in 3.5.4, except doubling the timeout
	- STP protocol must include 'simplified TCP sender' and 'fast retransmit'
	- Use concepts discussed e.g. 'seq numbers, cumulative acknowledgements, timers, buffers etc.'

	[5] Receiver should implement all features in 3.5.4.
	- You do NOT need to follow Table 3.2 for ACK generation
	- All packet should be immediately acknowledged. (no need to implement delayed ACKs)

	[6] STP is a byte-stream orientated protocol.
	- Include 'seq number' and 'acknowledgement number fields' in STP header for each segment
	- The meaning of seq number / acknowledgement number are the same in TCP

	[7] MSS (Maximum segment size) is max number of bytes of data that your STP segment can contain.
	- MSS counts data ONLY and does NOT include header.
	- Sender must be able to deal with diff values of MSS.
	- The value of MSS will be supplied to Sender as input argument.

	[8] Another input arg for Sender is Maximum Window Size (MWS)
	- MWS is the max number of un-acknowledged bytes that the Sender can have at any time.
	- MWS counts ONLY data / payload
	- Header len should NOT be counted as part of MWS
	you will be limiting
	the number of un-acknowledged bytes by using the MWS parameter. In other words, you will need
	to ensure that during the lifetime of the connection, the following condition is satisfied:
	'LastByteSent – LastByteAcked ≤ MWS'

	[9] Introduce artificial packet loss and delay.
	- Implement Packet Loss and Delay 'PLD' module as part of the sender program
	- Standard ver: PLD module only needs to drop packets
	- Extended ver: PLD module drop + delay packets
	- For simplicity, call both standard/ext versions PLD module

	[10] Use a 'constant timeout' in your program
	- Value of 'timeout' will be supplied to Sender as an input argument
	- This applies to standard ver of assignment
	- Ext has diff requirements

3.3 Features Excluded

	[1] Do not implement 'timeout estimation'
	[2] Do not implement 'double timeout interval'
	[3] Do not implement any 'flow or congestion control'
	[4] STP does not deal with 'corrupted packets'. Packets will be rarely corrupted.
	    Assume that packets can only be LOST, not corrupted.

3.4 Packet Header and MSS

	[1] Only include header fields that you think are necessary for STP
	- You can draw inspiraton from TCP but exact format of STP packet header is up to us.

	[2] Header portion can include as many fields as we think is necessary.
	- Two important fields are: 'Sequence number' and 'Acknowledgement number'
	- Also we need 'number of flags for connection and establishment teardown'
	
	[3] Data portion: must not contain more than MSS bytes of data
	- Use the same 'STP segment format for data transfer' as well as for
	  'acknowledgements flowing back from receiver -> sender.'
	- Only diff is acknowledgement segments will NOT contain any data.
	- All info necessary for proper functioning of your protocol must be provided in STP headers.
	- Dont use info from header of the UDP datagram that will encapsulate STP packets
	  (except port number and IP address)

3.5 Sender

	For standard ver of assignment, sender accepts the following 8 arguments:

[1] 'receiver_host_ip': IP address of Receivers host machine
[2] 'receiver_port': port number on which Receiver is expecting to receive packets from sender
[3] 'file.txt': name of text file that has to be transferred from sender->receiver using
                your reliable transport protocol
[4] 'MWS': max window size used by STP protocol in bytes
[5] 'MSS': max segment size = max data in bytes carried in each STP segment
[6]

















