#using inbuilt function
n=[7,5,3,6,9,2]
print(max(n))
print(min(n))

      #or
a=[7,5,3,6,9,2]
a.sort()
print(a[-1])
print(a[0])

#without using unbuilt function
x=[7,5,3,6,9,2]
min=x[0]
max=x[0]
for i in range(len(x)):
    if min>x[i]:
        min=x[i]
    elif max<x[i]:
        max=x[i]
print(min)
print(max)


from functools import reduce
list=[100,103,107,146,99]
max1=reduce(lambda a,b:a if a>b else b,list)
min1=reduce(lambda a,b:a if a<b else b,list)
print(max1)
print(min1)