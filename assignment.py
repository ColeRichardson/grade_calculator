import tkinter as tk

class Assignment:
	
	"""
	Attributes:
		- Name of assessment
		- Weight in decimal. float [0,1]
		- Mark in percent, float [0,100]
	"""
	def __init__(self, root, name=None, weight=None, mark=None, name_label=None, weight_label=None, mark_label=None):
		self.name = name
		self.weight = tk.Entry(root, bg='orange')
		self.mark = mark
		self.name_label = name_label
		self.weight_label = weight_label
		self.mark_label = mark_label

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
