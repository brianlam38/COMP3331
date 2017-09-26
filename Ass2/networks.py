#!/usr/bin/python3

from collections import *

# 2D Matrix Rep
class Graph:

	def __init__(self, num_nodes):
		self.num_nodes = 0
		self.nodes = set()					# routers
		self.edges = defaultdict(list)		# links
		self.delays = {}					# link delays
		self.cap = {}					# circuit capacity
		self.load = {}						# load = Active Circuits / Capacity

	def addNode(self, node):
		self.nodes.add(node)

	# !neighbour = infinite delay
	def addEdge(self, from_n, to_n, delay, capacity, active):
		# init link
		self.edges[from_n].append(to_n)
		self.edges[to_n].append(from_n)
		# init link delay
		self.delays[(from_n, to_n)] = delay
		self.delays[(to_n, from_n)] = delay
		# init link capacity and load
		self.cap[(from_n, to_n)] = capacity
		self.cap[(to_n, from_n)] = capacity
		self.load[(from_n, to_n)] = active
		self.load[(to_n, from_n)] = active


class NetTopology:

	def __init__(self):
		self.Graph = None

	def showGraph(self, graph):
		for n in graph.nodes:
			print("router = {}".format(n))
			for e in graph.edges[n]:
				print("nb: {} | delay: {} | capacity: {} | load: {}" \
				.format(e, graph.delays[(n, e)], graph.cap[(n, e)], graph.load[(n, e)]))
			print("-----------------")
		return None

if __name__ == '__main__':
	# init graph, nodes, edge and link values
	g = Graph(4)
	g.addNode('A')
	g.addNode('B')
	g.addNode('C')
	g.addNode('D')
	g.addEdge('A', 'B', 100, 10, 1)
	g.addEdge('B', 'C', 200, 20, 2)
	g.addEdge('C', 'D', 300, 30, 3)

	network = NetTopology()
	network.showGraph(g)





