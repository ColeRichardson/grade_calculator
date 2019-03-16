class Assignment:
	
	"""
	Attributes:
		- Name of assessment
		- Weight in decimal. float [0,1]
		- Mark in percent, float [0,100]
	"""
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		self.mark = None

	def getName(self):
		return self.name

	def getWeight(self):
		return self.weight

	def getMark(self):
		return self.mark

	def setName(self, new_Name):
		self.name = new_Name

	def setWeight(self, new_Weight):
		self.weight = new_Weight

	def setMark(self, new_Mark):
		self.mark = new_Mark