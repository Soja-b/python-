def add (x,y):
 return x+y
def sub (x,y):
  return x-y
def mul(x,y):
  return x*y
def div(x,y):
  return x/y
def pow(x,y):
  return x**y
def cal(num1,op,num2):
  if op =="+":
      return add(num1,num2)
  elif op =="-":
        return sub(num1,num2)
  elif op =="*":
        return mul(num1,num2)
  elif op =="/":
         return div(num1,num2)
  elif op =="**":
        return pow(num1,num2)
  else:
      print("wrong input")
print("calculator")
num1=int(input("enter a number"))
num2=int(input("enter the second number"))
op=input(enter the operator(+,-,*,/,**))
result=cal(num1,op,num2)
print("the result is:",result)
