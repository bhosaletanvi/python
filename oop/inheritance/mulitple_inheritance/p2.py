class A :
	name="tanvi"
class B :
	name ="Sayali"
	age=20
class C(A,B):
	name="Yash"
	def display(self):
		print(self.name);

c=C();
c.display()	