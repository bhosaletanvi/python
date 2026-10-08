class student :
	name=" ";	

	def __init__(self,name):
		self.name=name;

	def fun(self):
		print("Hello",self);

ob = student("Tanvi");
ob.fun();
print(ob);

ob = student("Yash");
ob.fun();
print(ob);

