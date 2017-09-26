#!/usr/bin/python3

import sys
from collections import *

"""
2D Matrix Graph Representation
"""
class Graph:

	def __init__(self):
		#self.num_nodes = 0
		self.nodes = set()					# switches/routers
		self.edges = defaultdict(list)		# links
		self.delays = {}					# link delays
		self.cap = {}						# circuit capacity
		self.load = {}						# load = Active Circuits / Capacity

	# add a new switch/router
	def addNode(self, node):
		self.nodes.add(node)

	# add a new link
	# !neighbour = infinite delay
	def addEdge(self, from_n, to_n, delay, capacity):
		# init link
		self.edges[from_n].append(to_n)
		self.edges[to_n].append(from_n)
		# init link delay
		self.delays[(from_n, to_n)] = delay
		self.delays[(to_n, from_n)] = delay
		# init link capacity
		self.cap[(from_n, to_n)] = capacity
		self.cap[(to_n, from_n)] = capacity

	#def updateLoadMethod(self) --> NOT STARTED
		# method to update current load on link,
		# depending on currtime / active time of link

"""
Routing Performance Methods
"""
class RoutingPerf:

	def __init__(self, g, top, work):
		self.graph = g
		self.topology = top
		self.workload = work

	# init graph topology: routers, delay, capacity
	def initTopCap(self):
		f = open(self.topology, "r")
		data = f.readlines()
		for line in data:
			line = line.split()
			x = line[0]; y = line[1]; delay = line[2]; cap = line[2]
			#print("x = {}, y = {}, delay = {}, cap = {}".format(x, y, delay, cap))
			self.graph.addNode(x)
			self.graph.addNode(y)
			self.graph.addEdge(x, y, delay, cap)

	# init VC requests
	def startRequests(self):
		return None

	# display graph nodes, links, link delay values, link capacity, curr link load
	# NOTE: curr link load set to None since load methods are not implemented yet
	def showGraph(self):
		for n in self.graph.nodes:
			print("router = {}".format(n))
			for e in self.graph.edges[n]:
				print("nb: {} | delay: {} | capacity: {} | load: {}" \
				.format(e, self.graph.delays[(n, e)], self.graph.cap[(n, e)], None))
			print("-----------------")
		return None

"""
Main Function
"""
if __name__ == '__main__':
	num_args = 6
	if len(sys.argv) != num_args:
		print("Usage: ./networks.py NETWORK_SCHEME ROUTING_SCHEME TOPOLOGY_FILE WORKLOAD_FILE PACKET_RATE")
	else:
		# empty graph
		graph = Graph()
		
		# grab argument objects
		NETWORK_SCHEME, ROUTING_SCHEME, TOPOLOGY_FILE, WORKLOAD_FILE, PACKET_RATE = sys.argv[1:]
		r = RoutingPerf(graph, TOPOLOGY_FILE, WORKLOAD_FILE)
		
		# init nodes, links, delay and capacity values
		r.initTopCap()

		# test
		r.showGraph()

		# start virtual connection requests
		r.startRequests()











