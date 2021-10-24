#eliminate common element in two list (using library methods)
a=[1,2,3,4,5]
b=[4,5,6,7,8]
m=set(a)
n=set(b)
print(list(m.intersection(n)))

#without using library methods
x=[1,2,3,4,5]
y=[4,5,6,7,8]
lst=[]
for i in x:
    if i in y:
        lst.append(i)
print(lst)

#eliminate common element in two string
a="hellow bala murugan"
b="bala chandar hellow"
lst=[]
for i in a.split():
    if i in b.split():
        lst.append(i)
print(" ".join(lst))