num1=int(input("enter  the total no:of days:"))
num2=int(input("enter the total no:of working days:"))
n=int(input("enter the no:of student:"))
student_list=[]
for i in range(n):
	name=input("enter the name of student:")
	num3=int(input("enter the no:of present days:"))
	percentage=(num3/num2)*100
	student_list.append((name,percentage))
	student_list.sort()
for j in student_list:
	print(j[0],j[1])

