class Host(object):
	"""docstring for Host"""
	def __init__(self):
		super(Host, self).__init__()
		self.id = None
		self.switchId = None

	def getId(self):
		return self.id

	def setId(self, id):
		self.id = id

	def getSwitchId(self):
		return self.switchId

	def setSwitchId(self, switchId):
		self.switchId = switchId
		