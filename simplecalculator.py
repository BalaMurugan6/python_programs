
#simple calculator using string concept

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
method=input("type which method apply")
a=int(input("value1"))
b=int(input("value2"))
if method==("add"):
    print(add(a,b))
elif method==("sub"):
    print(sub(a,b))
else:
    print("no number")