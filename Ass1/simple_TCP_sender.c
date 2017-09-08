/*
 * Assume sender is not constrained by TCP flow or congestion control, that data from above
 * is less than milliseconds in size, and that data transfer is in one direction only.
 */

NextSeqNum = InitialSeqNumber
SendBase = InitialSeqNumber

loop (forever) {
	switch (event)
		// 1. DATA RECEIVED FROM APP: encapsulate data -> pass seg to IP
		event: data received from app above
			create TCP segment with seq no. from NextSeqNum
			if (timer not running) {
				start timer
			}
			pass segment to IP
			NextSeqNum = NextSeqNum + length(data)
			break;
		// 2. TIMER TIMOUT
		event: timer timout
			retransmit not yet acknowledged segment with smallest seq no.
			start timer
			break;
		// 3. ACK RECEIPT
		event: ACK received, with ACK field value of y
			if (y > SendBase) {
				SendBase = y
				if (there are currently any not yet acknowledged segments) {
					start timer
				}
			}
			break;
}	/* end of loop forever */






