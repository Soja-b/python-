class rect:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		return (self.length*self.breadth)
	def peri(self):
		return 2*(self.length+self.breadth)
l=int(input("enter the length of the rectangle:"))
b=int(input("enter the breadth of the rectangle:"))
ob=rect(l,b)
print("the area of rectangle is:",ob.area())
print("the perimeter of rectangle is:",ob.peri())


