class Sender_Congestion_Window:
	CWND = small constant val
	SSThresh = large constant val
	duplicate_ACKs = 0
	timer = 0

	# Congestion Adjustment 1 (increase rate)
	def adjust_bandwidth():
		foreach RTT:
			if CWND < SSThresh:			# Slow-Start
				CWND += 1				#		Increase CWND by 1 packet
			if CWND >= SSThresh:		# Congestion Avoidance (Additive-Increase)
				CWND = CWND + (1/CWND)	#		Double CWND size

	# Congestion Adjustment 2 (decrease rate)						
	def dupACK():						# Sender detects 3 duplicate ACKS: quickly recover the lost packet
		if duplicate_ACKs == 3:			# Fast-Retransmission / Fast-Recovery:
			SSThresh, CWND = CWND/2		#	  Set both SSThresh, CWND = half of prev CWND

	# Congestion Adjustment 3 (decrease rate)
	def timeout():						# Timeout occurs: Slow-Start Restart
		SSThresh = CWND/2				#	  Until it reaches new SSThresh = half of prev CWND
		CWND = 1 MSS					#	  CWND = 1 MSS
