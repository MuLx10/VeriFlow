class TrieNode(object):
	"""docstring for TrieNode"""
	def __init__(self):
		super(TrieNode, self).__init__()
		self.ecs = set()
		self.leftChild = self.rightChild = self.starChild = None
		self.openLeft = self.openRight = False
		self.possibleLeftEC = self.possibleRightEC = None
		self.nodeValue = None
		self.advertisedInterval = None

	def getLeftChild(self):
		return self.leftChild;
	
	def setLeftChild(self, leftChild):
		self.leftChild = leftChild;
	
	def getRightChild(self):
		return self.rightChild;
	
	def setRightChild(self, rightChild):
		self.rightChild = rightChild;
	
	def isOpenLeft(self):
		return self.openLeft;
	
	def setOpenLeft(self, openLeft):
		self.openLeft = openLeft;
	
	def isOpenRight(self):
		return self.openRight;
	
	def setOpenRight(self, openRight):
		self.openRight = openRight;

	def getStarChild(self):
		return self.starChild;
	
	def setStarChild(self, starChild):
		self.starChild = starChild;


	def numberOfNonStarChildren(self):
		num = 0;
		if (self.rightChild):
			num+=1
		if (self.leftChild):
			num+=1
		return num
	

	def getPath(self):
		return self.getPossibleLeftEC();

	def setPath(self, path):
		self.setPossibleLeftEC(path);

	def getPossibleRightEC(self):
		return self.possibleRightEC;

	def setPossibleRightEC(self, possibleRighttEC):
		self.possibleRightEC = possibleRighttEC;

	def getPossibleLeftEC(self):
		return self.possibleLeftEC;

	def setPossibleLeftEC(self, possibleLeftEC):
		self.possibleLeftEC = possibleLeftEC;

	def getNodeValue(self):
		return self.nodeValue;

	def setNodeValue(self, nodeValue):
		self.nodeValue = nodeValue;

	def getEcs(self):
		return self.ecs;

	def setEcs(self, ecs):
		self.ecs = ecs;

	def addEC (self, ec):
		self.ecs.add(ec);

	def getAdvertisedInterval(self):
		return self.advertisedInterval;

	def setAdvertisedInterval(self, advertisedInterval):
		self.advertisedInterval = advertisedInterval;
