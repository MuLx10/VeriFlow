class Switch(object):
	"""docstring for Switch"""
	def __init__(self):
		super(Switch, self).__init__()
		self.id = None
		self.nextHops = []
		self.connectedHosts = []
		self.rules = []

	def getAssociatedRule(self, rulePrefix):
		for r in self.rules:
			if r.matches(rulePrefix):
				return r
		return None

	def getId(self): 
		return self.id;
	
	def setId(self, id):
		self.id = id;

	def addNextHop(self, nextHop):
		self.nextHops.append(nextHop);
	
	def addConnectedHost(self, id):
		self.connectedHosts.append(id);
	

	def getNextHops(self):
		return self.nextHops;

	def setNextHops(self, nextHops):
		self.nextHops = nextHops;

	def addRule(self, newRule):
		self.rules.insert(0, newRule);

	def setRules(self, rules):
		self.rules = rules
	
	def getRules(self):
		return self.rules;
	

	def getConnectedHosts(self): 
		return self.connectedHosts;

	def setConnectedHosts(self, connectedHosts):
		self.connectedHosts = connectedHosts;
	
