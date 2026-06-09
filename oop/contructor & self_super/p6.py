class student :
	age=0
	string="tanvi"

	def __init__(self,b,c):
		print(self)
		self.age=b
		self.name=c

s1=student(20,"tanvi")
s2=student(30,"sayali")

print(s1.age)
print(s2.age)
