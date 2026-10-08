class person :
	name =""
	def __init__(self,name):
		self.name=name;
	def display(self):
		print("Name Is : ",self.name);

class student(person):
	def __init__(self,name):
		super().__init__(name);

class Employee(person):
	def __init__(self,name):
		super().__init__(name);

s= student("tanvi");
s.display();

e = Employee("sayali");
e.display();