student={}
n=int(input("enter the  numberof students:"))
for i in range(0,n):
 name=input("enter the name of student:")
 percentage=input("enter the percentage of student:")
 student[name]=percentage
list=list(student.items())
list.sort(reverse =True)
print(list)
