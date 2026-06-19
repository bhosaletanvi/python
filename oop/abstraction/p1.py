from abc import ABC , abstractmethod
class student(ABC) :
	@abstractmethod 
	def education(self):
		print("b.tech")
class child(student):
	def education(self):
		print("coding")

c=child()
c.education();