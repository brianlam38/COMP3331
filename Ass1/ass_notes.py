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

Three major events to data transmission and re-transmission in the TCP sender.
1. Data received from the app above ->
2. Timer timout
3. ACK receipt



