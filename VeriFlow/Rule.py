
class Rule(object):
	"""docstring for Rule"""
	def __init__(self, prefix = None, switchId = None, nextHopId = None):
		super(Rule, self).__init__()
		self.prefix = prefix;
		self.switchId = switchId;
		self.nextHopId = nextHopId;


	def equals(self, obj):
		if obj is None:
			return False

		return obj.prefix == self.prefix and obj.switchId == self.switchId and obj.nextHopId == self.nextHopId

	def decodeIpMask(self, ipMask):
		splitMask = ipMask.split("/");
		splitIp = splitMask[0].split(".");
		output = "";
		for s in splitIp:
			intValue = int(s)
			output += self.toEightBitBinary(intValue)
		return output[:int(splitMask[1])]

	def toEightBitBinary(self, intValue):
		binaryString = bin(intValue)[2:];
		length = len(binaryString);
		for i in range(length, 8):
			binaryString = "0" + binaryString
		return binaryString

	def getPrefix(self):
		return self.prefix

	def setPrefix(self, prefix):
		self.prefix = self.decodeIpMask(prefix)

	def getSwitchId(self):
		return self.switchId

	def setSwitchId(self, switchId):
		self.switchId = switchId

	def getNextHopId(self):
		return self.nextHopId

	def setNextHopId(self, nextHopId):
		self.nextHopId = nextHopId

	def matches(self, rulePrefix):
		return rulePrefix.startsWith(prefix)
