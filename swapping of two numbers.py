

#swapping of two numbers with using third variable
x=5
y=10
temp=x
x=y
y=temp
print("the value of x after swapping {}".format(x))
print("the value of y after swapping {}".format(y))

#without using third variable
#1st method  (using rot two() method)
a=6
b=10
a,b=b,a
print(a)
print(b)

#2nd

x=65
y=67
x=x+y
y=x-y
x=x-y
print(x)
print(y)

#3rd

x=78
y=5
x=x^y
y=x^y
x=x^y
print(x)
print(y)

