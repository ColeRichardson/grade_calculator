from assignment import Assignment

class Course:
	def __init__(self):
		self.gradeList = []

	def addGrade(self, gr):
		self.gradeList.append(gr)


	
	def getWeightedAverage(self):
		"""
		>>> x = grade("quiz1", 0.1, 50)
		>>> y = grade("quiz2", 0.1, 60)
		>>> CSC258 = Course()
		>>> CSC258.addGrade(x)
		>>> CSC258.addGrade(y)
		>>> CSC258.getWeightedAverage()
		"""
		sum1 = 0
		weightsum = 0
		for i in self.gradeList:
			if (i.mark != None ):
				weightsum += i.getWeight()
				sum1 += i.getWeight() * i.getMark()
		return (sum1 / weightsum , weightsum)


x = Assignment("quiz1", 0.1)
y = Assignment("quiz2", 0.1)
x.setMark(50)
y.setMark(60)
CSC158=Course()
CSC158.addGrade(x)
CSC158.addGrade(y)
print(CSC158.getWeightedAverage())
