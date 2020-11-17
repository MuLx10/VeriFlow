class ForwardingGraph(object):
	"""docstring for ForwardingGraph"""
	def __init__(self):
		super(ForwardingGraph, self).__init__()
		self.forwardingGraph = set()

	def addToGraph(self, nextHopId):
		self.forwardingGraph.add(nextHopId)

	def getForwardingGraph(self):
		return self.forwardingGraph

	def setForwardingGraph(self, forwardingGraph):
		self.forwardingGraph = forwardingGraph

	def contains(self, id):
		return id in self.forwardingGraph
		