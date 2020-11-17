class NetworkError(object):
	"""docstring for NetworkError"""
	def __init__(self, arg):
		super(NetworkError, self).__init__()
		self.errorType = None
		self.ec = None
		self.startingPoint = None

	def getErrorType(self):
		return self.errorType;

	def setErrorType(self, errorType):
		self.errorType = errorType;

	def getEc(self):
		return self.ec;

	def setEc(self, ec):
		self.ec = ec;

	def getStartingPoint(self):
		return self.startingPoint;

	def setStartingPoint(self, startingPoint):
		self.startingPoint = startingPoint;

		