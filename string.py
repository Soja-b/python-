def is_palindrome(n):
  n_rev=n[::-1]
  if (n==n_rev):
    return True
  else:
    return False
n=(input("enter a string:"))
result = is_palindrome(n)
if(result==True):
 print("the string",n,"is palindrome")
else: 
 print("the string",n,"is not palindrome") 
