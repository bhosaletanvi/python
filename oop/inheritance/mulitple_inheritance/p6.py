class A :
	def __init__(self):
		print("in construct A")
class B :
	def __init__(self):
		print("in constuct B")
class C(A,B):
	def __init__(self):
		print("in construct C")
		A.__init__()
		B.__init__()
c=C();