class parent :
	def __init__(self,name,age):
		self.__name=name
		self.age=age

	def update_name(self,name):
		self.__name=name

	def get_name(self):
		return self.__name

p=parent("tanvi",21)
print(p.age)
name = p.get_name()
print(name)

p.update_name("sayali")
name = p.get_name()
print(name)	