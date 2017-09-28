#!/usr/bin/python3

import sys
from collections import *

"""
2D Matrix Graph Representation
"""
class Graph:

	def __init__(self):
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


"""
Routing Performance Program
"""
class RoutingPerf:

	def __init__(self, g, top, work):
		self.graph = g
		self.topology = top
		self.workload = work

	# init graph topology: routers, delay, capacity
	def initTopology(self):
		f = open(self.topology, "r")
		data = f.readlines()
		for line in data:
			line = line.split()
			x = line[0]; y = line[1]; delay = line[2]; cap = line[2]
			#print("x = {}, y = {}, delay = {}, cap = {}".format(x, y, delay, cap))
			self.graph.addNode(x)
			self.graph.addNode(y)
			self.graph.addEdge(x, y, int(delay), int(cap))

	# init VC requests
	def startRequests(self):
		return None

	# display graph nodes, links, link delay values, link capacity, curr link load
	# NOTE: curr link load set to None since workload methods are not implemented yet
	def showGraph(self):
		for n in self.graph.nodes:
			print("router = {}".format(n))
			for e in self.graph.edges[n]:
				print("nb: {} | delay: {} | capacity: {} | load: {}" \
				.format(e, self.graph.delays[(n, e)], self.graph.cap[(n, e)], None))
			print("-----------------")
		return None

"""
Shortest Hop (SHP)
"""
def ShortestHopPath(graph, source):
	# init visited = src, path, nodes
	visited = {source: 0}
	pred = {}
	nodes = set(graph.nodes)

	# while nodes not empty
	while nodes: 
		curr_node = None
		# grab neighbour node with lowest cost path
		for n in nodes:
			if n in visited:
				# init curr = src node
				if curr_node is None:
					curr_node = n
				# update lowest cost neighbour
				elif visited[n] < visited[curr_node]:
					curr_node = n
		if curr_node is None:
			break

		# remove curr node, grab curr delay so far
		nodes.remove(curr_node)
		curr_delay = visited[curr_node]

		# check connected edges
		for e in graph.edges[curr_node]:
			delay = curr_delay + 1
			# if edge !visited, update new path
			if e not in visited:
				visited[e] = delay
				pred[e] = curr_node

	print("MST {}".format(pred))
	print("SHP FROM {} {}\n".format(source, visited))
	return visited, pred

"""
Shortest Delay Path (SDP)
"""
def ShortestDelayPath(graph, source):
	# init visited = src, path, nodes
	visited = {source: 0}
	pred = {}
	nodes = set(graph.nodes)

	while True: 
		min_node = None
		# pick unvisited node with lowest delay
		for n in nodes:
			if n in visited:
				if min_node is None:
					min_node = n
				elif visited[n] < visited[min_node]:
					min_node = n
		# all nodes visited, exit djikstras
		if min_node is None:
			break

		# grab min_node delay + remove min_node from set
		nodes.remove(min_node)
		curr_delay = visited[min_node]

		# calculate distance to each unvisited neighbour
		# edge relaxation
		for e in graph.edges[min_node]:
			delay = curr_delay + graph.delays[(min_node, e)]
			# if link delay < known link delay, update new path
			if e not in visited or delay < visited[e]:
				visited[e] = delay
				pred[e] = min_node


	print("MST {}".format(pred))
	print("SDP FROM {} {}\n".format(source, visited))
	return visited, pred

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
		r.initTopology()

		# test
		r.showGraph()

		# start virtual connection requests
		r.startRequests()

		# Select scheme
		if ROUTING_SCHEME == "SHP":
			print("[ SCHEME: SHORTEST HOP PATH ]")
			SHP = ShortestHopPath(r.graph, 'A')
		elif ROUTING_SCHEME == "SDP":
			print("[ SCHEME: SHORTEST DELAY PATH ]")
			SDP = ShortestDelayPath(r.graph, 'A')











