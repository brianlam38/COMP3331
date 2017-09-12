Chapter 3.5.3 Round-Trip Time Estimation and Timeout

TCP uses a timeout/retransmit mechanism to recover lost segments.
Timeout should be larger than the connections RTT = time from segment sent -> segment acknowledged.
-> Otherwise unnecessary transmissions would be sent.
-> But how much larger?
-> How to estimate RTT in the first place?
-> Should a timer be associated with each and every unacknowledged segment?

ESTIMATING ROUND-TRIP TIME 

SampleRTT = amount of time between seg sent / passed to IP -> ack seg received
-> TCP implementations take only one SampleRTT measurement at a time.
-> This means a new value of SampleRTT once every RTT.
-> Only computes SampleRTT for segments that have only been transmitted once (NOT retransmitted)
