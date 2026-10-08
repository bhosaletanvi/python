class parent :
	def __init__(self,name ,age):
		self.name=name
		self.__age=age

	def get_age(self):
		print(self.__age)

class child(parent):
	def __init__(self,name,age,rollno):
		super().__init__(name,age)
		self.rollno=rollno

	def display(self):
		print(self.name)
		print(self.rollno)
		self.get_age();

c=child("tanvi",21,80)
c.display();