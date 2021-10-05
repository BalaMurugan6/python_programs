
#to find factorial of number
num=int(input("enter your number"))
factorial=1
if num>=0:
    for i in range(2,num+1):
        factorial = factorial * i
    print(f"the factorial of the {num} is {factorial}")
else:
    print("negative value of factorial doesn't exist")


#simple way
import math
x=int(input("enter the number"))
try:
 a=math.factorial(x)
 print(f"the factorial number of {x} is {a}")
except:
    print("can't find factorial for negative number")

#using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter the number"))
print(fact(n))
