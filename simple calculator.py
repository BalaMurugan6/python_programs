

#simple calculator using int concept

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
print(""""select your method
1.add
2.sub
3.mul""")
method=int(input("enter your method"))
a=int(input("number1"))
b=int(input("number2"))
if method==1:
    print(add(a,b))
elif method==2:
    print(sub(a,b))
elif method==3:
    print(mul(a,b))
else:
    print("unavailable")