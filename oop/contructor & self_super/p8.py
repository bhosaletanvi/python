class person :
	name="";
	age=0;
	add="";
	
	def __init__(self,name,age,add):
		self.name=name;
		self.age=age;
		self.add=add;

class student(person):
	marks=0;
	
	def __init__(self,name,age,add,marks):
		self.marks=marks;
		super().__init__(name,age,add);

p = person("Tanvi",19,"satara")
p1 = person("sayali",29,"pune")

s= student("Tanvi",19,"satara",80)
s1= student("abc",39,"whj",39)
print(p1.name)
print(p.name)
print(s.name)
print(s1.name)



