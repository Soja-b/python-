print("rectangle---------:")


l=int(input("enter length of rectangle:"))
b=int(input("enter breadth of rectangle:"))
area=lambda l,b:l*b
print("area of rectanle:",area(l,b))
peremeter=lambda l,b:2*l+b
print("peremeter of rectangle is:",peremeter(l,b))
print("square-------:")


le=int(input("enter the side of square:"))
a=lambda le:le*le
print("area of square is:",a(le))
peri=lambda le:4*le
print("peremeter of the square is:",peri(le))

