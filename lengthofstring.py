n=int(input("enter the limit:"))
a=[]
for x in range(0,n):
	elements=input("enter the elements of  list:")
	a.append(elements)
max=len(a[0])
temp=a[0]
for i in a:
 if (len(i)>max):
 	max=len(i)
 	temp=i
print(" The largest word is:",temp)
 
