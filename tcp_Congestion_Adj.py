class Sender_Congestion_Window:
	CWND = small constant val
	SSThresh = large constant val
	duplicate_ACKs = 0
	timer = 0
	MSS = 1

	# Congestion Adjustment 1 (increase rate)
	def adjust_bandwidth():
		foreach RTT:

			if CWND < SSThresh:			 # STATE 1: Slow-Start
				CWND += MSS				 #		Increase CWND by 1 packet (as MSS = 1).
										 #		Ramp up exponentially for efficiency

			if CWND >= SSThresh:		 # STATE 2: Congestion Avoidance (Additive-Increase)
				CWND = CWND + (MSS/CWND) #		Increase CWND by 1/CWND
										 #		Ramp up consistently

	# Congestion Adjustment 2 (decrease rate)						
	def dupACK():						 # Sender detects 3 duplicate ACKS: quickly recover the lost pkt
		if duplicate_ACKs == 3:			 # Fast-Retransmission:
			SSThresh, CWND = CWND/2		 #	  Set both SSThresh, CWND = half of prev CWND

	# Congestion Adjustment 3 (decrease rate)
	def timeout():						 # Timeout occurs: Slow-Start Restart
		SSThresh = CWND/2				 #	  Until it reaches new SSThresh = half of prev CWND
		CWND = 1 MSS					 #	  CWND = 1 MSS

	# Summary: INCREASE 1 = Slow-Start				CWND = CWND + MSS
	#		   INCREASE 2 = Congestion-Avoidance	CWND = CWND + MSS/CWND
	#
	#		   DECREASE 1 = dupACK 					SSThresh = CWND/2 , CWND = CWND/2
	#		   DECREASE 2 = timeout 				SSThresh = CWND/2 , CWND = 1 MSS


# NOTE: With Fast-Retransmission, time is not lost waiting for a
#       timeout in order for retransmission to begin