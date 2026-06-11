class A:
	def fun(self):
		print("in class A");

class B :
	def fun(self):
		print("in class B")

class C(A,B):
	def fun(self):
		print("in class C")
c=C();
c.fun();