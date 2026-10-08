class person :
	name ="Tanvi"
class student(person):
	name="Sayali"
	def display(self):
		print("Name is :",super().name)

s=student();
s.display();	