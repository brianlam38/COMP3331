# Principles of Reliable Data Transfer
# Reliable Data Transfer = RDT

# Introduction
With RDT, transferred data bits are: 'not corrupted' | 'not lost' | 'delivered in order'
- TCP offers this service model to internet applications that use it
- However, layers below RDT Protocol may be unreliable.

'rdt_send()' = Pass data from sender-side app to be delivered to the receiver-side app
'rdt_rcv()' = Called when packet arrives to receiver-side channel
'deliver_data()' = Delivers the data to receiver-side app

