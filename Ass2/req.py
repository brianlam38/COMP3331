RoutingPerformance Program
[1] NETWORK_SCHEME: Type of network
-> VIRTUAL CIRCUIT NETWORK or VIRTUAL PACKET NETWORK
[2] ROUTING_SCHEME: Routing scheme
-> Three routing protocols (variants of djikstras)
	-> SHP: Shortest Hop Path
	-> SDP: Shortest Delay Path
	-> LLP: Least Loaded Path
[3] TOPOLOGY FILE: Network topology specs
[4] WORKLOAD FILE: Virtual connection requests in the network
[5] PACKET_RATE: +ve int, showing no. pkts per second for each virtual connection

For TOPOLOGY FILE:
-> Will be using both a virtual circuit / virtual packet network to evaluate performance of routing protocols
-> A routing protocol is required in  BOTH networks to determine path btwn src -> dest of a virtual circuit
-> Main diff btwn circuit / packet network is how end-to-end path is determined
	-> One virtual connection to circuit network follows the same for transmitting all packets.
	-> One virtual connection in packet network uses routing protocol to determine path for each packet independently.
	   Therefore, a virtual connection needs to invoke routing protocol N times, where N = num pkts trasnmitted through the connection
	   I.e. one virtual connection in virtual packet network has N virtual circuits for transmitting N packets
-> Tolopogy file example:
For Routers A B C D
A B 10 19				5 links connecting all 4 nodes (router = nodes)
A C 15 20		Example: Node A -> Node C , one-way propagation delay of 10ms , capacity = 19 simultaneous circuits
B C 20 2		All links are bi-directional , with identical propagation delay in both directions
B D 30 70		Each link consumes 1 unit resource , with at most 1 direct link between two nodes in the graph
C D 8 20		Assume the topology will form a CONNECTED GRAPH (no isolated nodes)

-> First task for your program is to read the topology file and construct a suitable internal
   representation of the network topology, using an appropriate data structure.
-> Refer to standard reps of undirected graphs, which is most appropriate way to model the network
-> All node names are A-Z uppercase alphabetical = max 26 nodes
-> Propagation delays d are +ve ints (0 < d < 200) expressed in milliseconds
-> All link capacities are +ve ints (0 < C < 100) and indicate no. of virtual connections supported by a link

For WOROKLOAD_FILE:
-> Virtual circuit requests arrive in the network will be specified in the virtual connection requests in this file.

SUMMARY:
Nodes A, B
A B 10 19
A -> B = Link A to B | 10ms propagaton delay | 19 supported simultaneous connections (circuits)

BRIANS TASK 
-> TAKE IN NETWORK TOPOLOGY FILE THEN REPRESENT THE ITEMS IN A DATA STRUCTURE






