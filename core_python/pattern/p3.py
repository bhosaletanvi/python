odd=1
even=2
for i in range (0,3) :
	for j in range(0,3) :
		if(i%2==0):
			print(odd,end=" ")
			odd+=2
		else:
			print(even,end=" ")
			even+=2

	print()