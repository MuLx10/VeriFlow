from VeriFlow.TrieNode import TrieNode
from VeriFlow.Interval import Interval

class Trie(object):
	"""docstring for Trie"""
	def __init__(self):
		super(Trie, self).__init__()
		self.root = TrieNode()
		self.root.setStarChild(TrieNode())
		self.ecs = set()

	def getRoot(self):
		return self.root

	def setRoot(self, root):
		self.root = root

	# def deleteFromTrie(self, prefix):
	# 	return self.deleteFromTrie(prefix + "*", root, "")

	def deleteFromTrie(self, ip, node = None, path = ""):
		if (node is None):
			node = self.root
		generatedEcs = []
		currentChar = ip[0];
		if (currentChar == '*'):
			if (node.getStarChild() == None):
				print("No such rule to be deleted!");
				return set()
			
			node.setStarChild(None);
			if (node.numberOfNonStarChildren() == 0):
				node.setNodeValue(0);
				return set()
			
			nodeValue = 0;
			if (node.numberOfNonStarChildren() == 2):
				nodeValue = node.getRightChild().getNodeValue() + node.getLeftChild().getNodeValue();
				if (node.getLeftChild().isOpenRight() or node.getRightChild().isOpenLeft()):
					nodeValue+=1;
			
			elif (node.getLeftChild() != None):
				node.setOpenLeft(node.getLeftChild().isOpenLeft());
				nodeValue = node.getLeftChild().getNodeValue();
			else:
				node.setOpenRight(node.getRightChild().isOpenRight());
				nodeValue = node.getRightChild().getNodeValue();
			node.setNodeValue(nodeValue);

		elif (currentChar == '0'):
			isNew = node.getLeftChild() == None;
			if (isNew):
				print("No such rule to be deleted!");
				return set();
			
			ecLeft = self.deleteFromTrie(ip[1:], node.getLeftChild(), path + "0");
			generatedEcs.extend(list(ecLeft)); 
		else:
			isNew = node.getRightChild() == None;
			if (isNew):
				print("No such rule to be deleted!");
				return set();
	
			ecRight = self.deleteFromTrie(ip[1:], node.getRightChild(), path + "1");
			generatedEcs.extend(list(ecRight));
		
		generatedEcs.extend(list(self.updateNode(node, path)));
		return set(generatedEcs);


	def insertIntoTrie(self, ip, node = None, path = ""):
		if(node is None):
			node = self.root

		ecSet = [];
		currentChar = ip[0];
		if (currentChar == '*'):
			node.setStarChild(TrieNode());
			node.setOpenLeft(False);
			node.setOpenRight(False);

		elif (currentChar == '0'):
			isNew = node.getLeftChild() == None;
			if (isNew):
				node.setLeftChild(TrieNode());
			ecS1 = self.insertIntoTrie(ip[1:], node.getLeftChild(), path + "0");
			ecSet.extend(list(ecS1));
		else:
			isNew = node.getRightChild() == None;
			if (isNew):
				node.setRightChild(TrieNode());
			ecS2 = self.insertIntoTrie(ip[1:], node.getRightChild(), path + "1");
			ecSet.extend(list(ecS2));

		upn = self.updateNode(node, path)
		ecSet.extend(upn)
		return set(ecSet);

	def updateNode(self, node, path):
		nodeValue = 0;

		newEcs, generatedEcs = set(), set()
		oldECs = node.getEcs();

		if (node.getLeftChild() != None):
			if (node.getLeftChild().getNodeValue() == 0):
				node.setLeftChild(None);
		if (node.getRightChild() != None):
			if (node.getRightChild().getNodeValue() == 0):
				node.setRightChild(None);

		if(node.numberOfNonStarChildren() == 2):
			if (node.getLeftChild().isOpenRight() or node.getRightChild().isOpenLeft()):
				generatedEcs.add(Interval(node.getLeftChild().getAdvertisedInterval().getRight(), node.getRightChild().getAdvertisedInterval().getLeft()));
			
			nodeValue = node.getLeftChild().getNodeValue() + node.getRightChild().getNodeValue();
			if (node.getStarChild() != None):
				if (node.getLeftChild().isOpenLeft()):
					generatedEcs.add(Interval(path, node.getLeftChild().getAdvertisedInterval().getLeft()));
					nodeValue+=1;
				if (node.getRightChild().isOpenRight()):
					generatedEcs.add(Interval(node.getRightChild().getAdvertisedInterval().getRight(), self.binaryAdd(path, 1)));
					nodeValue+=1;
				node.setAdvertisedInterval(Interval(path, self.binaryAdd(path, 1)));

			else:
				node.setAdvertisedInterval(Interval(node.getLeftChild().getAdvertisedInterval().getLeft(), node.getRightChild().getAdvertisedInterval().getRight()));
				node.setOpenLeft(node.getLeftChild().isOpenLeft());
				node.setOpenRight(node.getRightChild().isOpenRight());

			if (node.getRightChild().isOpenLeft() or node.getLeftChild().isOpenRight()):
				nodeValue+=1;

		elif(node.numberOfNonStarChildren() == 1):
			if (node.getLeftChild() != None):
				nodeValue = node.getLeftChild().getNodeValue();
				node.setOpenLeft(node.getLeftChild().isOpenLeft());
				node.setOpenRight(True);
				if (node.getStarChild() != None):
					generatedEcs.add(Interval(node.getLeftChild().getAdvertisedInterval().getRight(), self.binaryAdd(path, 1)));
					nodeValue += 1;
					if (node.isOpenLeft()):
						generatedEcs.add(Interval(path, node.getLeftChild().getAdvertisedInterval().getLeft()));
						nodeValue+=1;
					node.setAdvertisedInterval(Interval(path, self.binaryAdd(path, 1)));
					node.setOpenLeft(False);
					node.setOpenRight(False);
				else:
					node.setAdvertisedInterval(node.getLeftChild().getAdvertisedInterval());
			else:
				nodeValue = node.getRightChild().getNodeValue();
				node.setOpenRight(node.getRightChild().isOpenRight());
				node.setOpenLeft(True);
				if (node.getStarChild() != None) :
					generatedEcs.add(Interval(path, node.getRightChild().getAdvertisedInterval().getLeft()));
					nodeValue+=1;
					if (node.isOpenRight()):
						generatedEcs.add(Interval(node.getRightChild().getAdvertisedInterval().getRight(), self.binaryAdd(path, 1)));
						nodeValue+=1;
					node.setAdvertisedInterval(Interval(path, self.binaryAdd(path, 1)));
					node.setOpenLeft(False);
					node.setOpenRight(False);
				else:
					node.setAdvertisedInterval(node.getRightChild().getAdvertisedInterval());
		elif(node.numberOfNonStarChildren() == 0):
			nodeValue = 1;
			node.setOpenLeft(False);
			node.setOpenRight(False);
			node.setAdvertisedInterval(Interval(path, self.binaryAdd(path, 1)));
			generatedEcs.add(node.getAdvertisedInterval());
		

		for i in  generatedEcs:
			if (i not in oldECs):
				newEcs.add(i);
		node.setEcs(generatedEcs);
		node.setNodeValue(nodeValue);
		return newEcs;

	def getECListFromTrie(self, node = None):
		if(node is None):
			node = self.root
		ecs = [];
		if (node.getRightChild() != None):
			ecs.extend(list(self.getECListFromTrie(node.getRightChild())));
		if (node.getLeftChild() != None):
			ecs.extend(list(self.getECListFromTrie(node.getLeftChild())));
		ecs.extend(list(node.getEcs()));
		return set(ecs);
	

	def numberOfECs(self):
		return self.root.getNodeValue();

	def addRule(self, rule):
		return self.insertIntoTrie(rule.getPrefix() + "*", self.root,  "");

	def getEcs(self): 
		return ecs;

	def setEcs(self, ecs):
		self.ecs = ecs;
	

	def generateECs(self):
		self.ecs.clear();
		generateECs(root, "");
		return ecs;
	

	def generateECs(self, node, path):

		if(node.numberOfNonStarChildren() == 2):
			ecLeft = generateECs(node.getLeftChild(), path + "0");
			ecRight = generateECs(node.getRightChild(), path + "1");
			if (node.getLeftChild().isOpenRight() or node.getRightChild().isOpenLeft()):
				ecs.add(Interval(ecLeft.getRight(), ecRight.getLeft()));
			if (node.getStarChild() != None):
				if (node.getLeftChild().isOpenLeft()):
					ecs.add(Interval(path, ecLeft.getLeft()));
				if (node.getRightChild().isOpenRight()):
					ecs.add(Interval(ecRight.getRight(), self.binaryAdd(path, 1)));
				node.setAdvertisedInterval(Interval(path, self.binaryAdd(path, 1)));
				return node.getAdvertisedInterval();
			else:
				node.setAdvertisedInterval(Interval(ecLeft.getLeft(), ecRight.getRight()));
				return node.getAdvertisedInterval();
		
		elif(node.numberOfNonStarChildren() == 1):
			if (node.getLeftChild() != None):
				ecLeft = generateECs(node.getLeftChild(), path + "0");
				if (node.getStarChild() != None):
					ecs.add(Interval(ecLeft.getRight(), self.binaryAdd(path, 1)));
					if (node.getLeftChild().isOpenLeft()):
						ecs.add(Interval(path, ecLeft.getLeft()));
					node.setAdvertisedInterval(Interval(path, self.binaryAdd(path, 1)));
					return node.getAdvertisedInterval();

				node.setAdvertisedInterval(ecLeft);
				return node.getAdvertisedInterval();

			else:
				ecRight = generateECs(node.getRightChild(), path + "1");
				if (node.getStarChild() != None):
					ecs.add(Interval(path, ecRight.getLeft()));
					if (node.getRightChild().isOpenRight()):
						ecs.add(Interval(ecRight.getRight(), self.binaryAdd(path, 1)));
					node.setAdvertisedInterval(Interval(path, self.binaryAdd(path, 1)));
					return node.getAdvertisedInterval();
				node.setAdvertisedInterval(ecRight);
				return ecRight;
		elif(node.numberOfNonStarChildren() == 0):
			e = Interval(path, self.binaryAdd(path, 1));
			ecs.add(e);
			node.setAdvertisedInterval(e);
			return e;
		
		assert (False);
		return None;
	

	def intToBinaryString(self, intValue, numDigits):
		binaryString = bin(intValue)[2:];
		length = len(binaryString);
		for i in range(length, numDigits):
			binaryString = "0" + binaryString
		return binaryString

	def binaryAdd(self, path, i):
		if (path == ""):
			return "End";
		decimal = int(path, 2);
		decimal += i;
		return self.intToBinaryString(decimal, len(path));

