from abc import ABC , abstractmethod
class student(ABC) :
	name=""
	def __init__(self,name):
		self.name

	@abstractmethod 
	def education(self):
		print("b.tech")

	def display(self):
		print(self.name)

class child(student):
	def __init__(self,name):
		super().__init__(name)
	def education(self):
		print("coding")

c=child("tanvi")
c.education();
c.display()