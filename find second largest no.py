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
z=[390,99,23,89,899,100,98,900]
max1=max2=0
for i in range(len(z)):
    if max1<z[i]:
        max1=z[i]
for j in range(len(z)):
    if max2<z[j]:
        if max1!=z[j]:
            max2=z[j]
print(max1)
print(max2)



