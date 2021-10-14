#find 2nd largest using sort
a=[45,98,99,23]
b=sorted(a)
print(b[-2])

#find 2nd largest without using sort
y=[10,20,4,45,99]
y.remove(max(y))
print(max(y))

#find 3rd largest without using sort
x=[10,20,4,45,99]
x.remove(max(x))
x.remove(max(x))
print(max(x))

#find 1st & 2nd largest without using sort

z=[67,99,23,89,100,98]
max1=max2=z[0]
for i in range(len(z)):
    if max1<z[i]:
        max2=max1
        max1=z[i]
    elif (max2<z[i] and max1>z[i]):
        max2=z[i]
print(max1)
print(max2)

