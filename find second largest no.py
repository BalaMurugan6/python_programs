
#find 2nd largest using sort

a=[45,98,99,23]
b=sorted(a)
print(b[-2])

#find 2nd largest without using sort

x=[10,20,4,45,99]
x.remove(max(x))
print(max(x))

#find 3rd largest without using sort

x=[10,20,4,45,99]
x.remove(max(x))
x.remove(max(x))
print(max(x))


