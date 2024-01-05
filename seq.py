def recr_fibo(n):
 if n<=1:
    return n
 else:
   return(fibo(n-1)+recur_fibo(n-2))
 n=int(input("enter the number of terms:"))
 print("fib sequence:")
 for i in range(n):
   print(fib(i))
