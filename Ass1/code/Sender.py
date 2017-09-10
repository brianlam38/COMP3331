# Simple Transport Protocol (STP)
#
# Sender side program
# 
# Three major components to data transmission and re-transmission:
# 1. Data received from app layer above
# 2. Timer timeout
# 3. ACK receipt

class STPPacket:
	def __init_(self, data, seq_num, ack_num, ack=False, syn=False, fin=False)
		self.data = data
		self.seq_num = seq_num
		self.ack_num = akc_num
		self.ack = ack
		self.syn = syn
		self.fin = fin

class Receiver:
	# you need to create this
	# receiver needs to have a sequence number so it can deal with out-of-order pakes
	# receiver receives stp_packet and then writes the data inside the packet


class Sender:
	# you need to create this.
	# a lot more complicated, but just follow the assignment spec
	# you can do go-back-N, selective repeat, whatever works
	# also need sequence number

# how to create packet?
myPacket = Packet(data, 0, 0, True, False, False)

# Packet is an object. How to send and receive this over UDP?

# send
import pickle
stp_packet = STPPacket(data, . . .)
socket.sendto(pickle.dumps(stp_packet), (client_ip, client_port))

# receive
import pickle
data, addr = socket.recvfrom(4096)
stp_packet = pickle.loads(data)

################################
# DATA RECEIVED FROM APP LAYER
################################

# Sender waits for data to be passed down from app layer
wait()

# stp_send(data) is called by app layer.
stp_send(data)

# send packet via. udp_send
# -> sender reads file + creates STP Segment (seq num + packet sndpkt + checksum)
# -> create and transmit UDP datagram + UDP send
# -> start timer (if another time is not already running from another segment)
#    timer is associated the oldest unacknowledged segment
sndpkt = make_pkt(0, data, checksum)
udt_send(sendpkt)
start_timer

##########################
# WAIT FOR RESPONSE - NAK
##########################

# if waiting, can't receive more data from app layer = stp_send() can't occur

# ACK response packet comes back
stp_rcv(rcvpkt) && isACK

# NAK response packet comes back
stp_rcv(rcvpkt) && isNAK
retransmit


##########################
# WAIT FOR RESPONSE - NAK
##########################







