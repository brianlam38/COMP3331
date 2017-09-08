# NOTES FOR ASSIGMENT 1

Implement a reliable transport protocol over UDP. -> Simple Transport Protocol 'STP'

Features include 'common features in many transport protocols':
-> timeout
-> ACK
-> sequence number

The assignment imitiates some multimedia services on the internet, where companies
have implemented their own proprietary transport protocols over UDP, e.g. QUIC for Google Chrome.

QUIC 'Quick UDP Internet Connection'
-> Great for gaming, streaming media, VoIP services
-> For these services, you want low overhead to reduce latency and if the server
   didnt receive your latest mouse movement, theres no need to spend a scond or two to
   fix that because the action has already moved on.
-> However, this wouldnt be suitable for requesting a website because you cant guarantee
   that all the data would make it.

--------

Basic setup of the assignment:
-> File is to be transferred from the Sender to the Receiver.
-> Sender will run on the sender-side while Receiver runs on the receiver-side.
-> Note: data segments will flow from the sender to the receiver, while ACK segments will flow
   from the receiver to the sender.

TWO VERSIONS: Standard + Extended




