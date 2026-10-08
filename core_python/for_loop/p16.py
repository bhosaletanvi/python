n = 4
ans=0
for a in range (2,n+1) :
	if(n%a==0):
		ans=a
		break
if(ans==n):
	print("Prime Number")
else :
	print("not prime number")