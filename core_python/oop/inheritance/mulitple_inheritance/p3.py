class A :
	name="tanvi"
class B :
	name="Sayali"
class C(B,A):
	def display(self): 
		print(self.name)

c=C();
c.display()
