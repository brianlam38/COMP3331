# Reliable Data Transfer

IP does not guarantee:
-> datagram delivery | datagram in-order delivery | datagram integrity
With IP, datagrams can:
-> Never reach dest | arrive out of order | become corrupted, bits flipped

'NOTE: Datagrams'
-> Dont care whether data is reached to its dest or not, nor errors occurred during transmission.
-> UDP uses Datagrams

TCP creates reliable data transfer on top of IP.
-> While TCP is great in theory, timer management can require considerable overhead.
-> Recommended TCP timer management system = use only a single transmission tier

# Three major events to TCP data transmission

Three major events to data transmission and re-transmission in the TCP sender.
1. Data received from the app above
2. Timer timout
3. ACK receipt

'FIRST EVENT: TCP receives data'
On occurrence of event:
-> TCP encapsulates data in a segment
-> TCP passes seg to IP
Each segment includes a sequence number that is the byte-stream number of the 1st data byte in
the segment.

If the timer is not already running for another segment, TCP starts the timer when the segment
is passed to IP (The timer is associated w/ the oldest unacknowledged segment)

Expiration interval for the timer = TimeoutInterval, calculated from EstimatedETT and DEVRTT.

--- REFER TO SIMPLIFIED TCP SENDER C PROGRAM IN DIR ---

'SECOND EVENT: Timer timeout'
On occurrence of event:
-> TCP responds to timout by retransmitting the segment that caused timeout
-> TCP then restarts the timer

'THIRD EVENT: Arrival of an Acknowledgement segment ACK from the RECEIVER'
On occurence of event:
-> TCP compares ACK value y with variable SendBase.
   TCP state var SendBase = seq no. of the oldest unacknowledged byte.
   SendBase-1 = seq no. of the last byte that is known to have been received correctly and in-order at receiver.
-> TCP uses cumulative acknowledgements, so 'y' acknowledges receipt of all bytes before byte number 'y'
   If 'y > SendBase' then ACK is acknowledging one or more previously unacknowledged segments.
   Thus, sender updates its 'SendBase' var.
   It also restarts the timer if there currently arent any not yet acknowledged segments






















