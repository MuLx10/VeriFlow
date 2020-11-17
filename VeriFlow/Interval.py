class Interval(object):
	"""docstring for Interval"""
	def __init__(self, left, right):
		super(Interval, self).__init__()
		self.left = left
		self.right = right

	def getRight(self):
		return self.right

	def setRight(self, right):
		self.right = right

	def getLeft(self):
		return self.left

	def setLeft(self, left):
		self.left = left
	

	def hashCode(self):
		return Objects.hash(left, right)

	def equals(self, obj) :
		if obj is None:
			return False
		try:
			eq = self.left == obj.left and self.right == obj.right
		except Exception as e:
			eq = False
		return eq

	def toString(self):
		return "[" + left + "," + right + ")"
