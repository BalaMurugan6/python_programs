#fibonacci series it generates given number of the times
#n=int(input("enter the numbers"))
#first=0
#second=1
#for i in range(n):
#   third=first+second
#   first=second
#   second=third
#   print(first)

#fibonacci series it generates within a range of given number
x=int(input("enter the numbers"))
first=0
second=1
while second<x:
   third=first+second
   first=second
   second=third
   print(first)

#using recursion
def fib(n):
   if n<=1:
      return n
   else:
      return fib(n-1)+fib(n-2)
n=int(input("enter the number"))
print("Fibonacci series")
for i in range(n):
   print(fib(i))








