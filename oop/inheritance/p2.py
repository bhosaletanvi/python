class parent :
	def property(self):
		print("2 acr")
	
class child(parent):
	def education(self):
		print("B.tech")
c1=child();
c1.property();
c1.education();