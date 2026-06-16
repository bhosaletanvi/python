class parent :

	def __init__(self,name,age):
		self.name=name
		self.age=age

class child(parent):
	def __init__(self,name,age):
		super().__init__(name,age)
	def display(self):
		print("name : ",self.name)
		print("age :",self.age)

c=child("tanvi" , 21);
c.display();
print(c.name)