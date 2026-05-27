class person:
	name=" ";
	add=" ";
	age=0;
	
	def __init__(self,name,add,age):
		self.name=name;
		self.add=add;
		self.age=age;

class student(person):
	roll_no =0;
	marks=0;

	def __init__(self,marks,roll_no,name,add,age):
		super().__init__(name,add,age);
		self.marks=marks;
		self.roll_no=roll_no;
		

s1= student(69,3,"abc","satara",21);
print(s1.name)
print(s1.add)
print(s1.age)
print(s1.marks)
print(s1.roll_no)
