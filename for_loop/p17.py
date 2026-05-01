n = 7
count=0
for a in range (1,n+1) :
	if(n%a==0):
		count+=1
if(count==2):
	print("Prime Number")
else :
	print("not prime number")