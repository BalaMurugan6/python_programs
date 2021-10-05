#concatenate two lists in the following order
list1=["hellow","hi"]
list2=["divya","sam"]
list3=[]
for i in list1:
    for j in list2:
     x=i+j
     list3.append(x)
print(list3)

lst1=[34,76,67,45]
lst2=[23,98,53,85]
lst3=[]
for i in range(len(lst1)):
    lst3.append(lst1[i]+lst2[i])
print(lst3)

      #or

lst1=[34,76,67,45]
lst2=[23,98,53,85]
x=list(map(lambda a,b:a+b,lst1,lst2))
print(x)

#sum of single list
lst1=[45,87,76,76]
print(sum(lst1))

          #or
lst=[45,87,76,76]
sum=0
for i in lst:
    sum=sum+i
print(sum)

     #or
from functools import reduce
lst1=[45,87,76,76]
x=reduce(lambda a,b:a+b,lst1)
print(x)

#Write a Python program to create a list by concatenating a given list which range goes from 1 to n

my_list = ['p', 'q']
n = 4
new_list = [x+str(y) for y in range(1,n+1) for x in my_list]
print(new_list)
       #OR

my_list = ['p', 'q']
n = 4
lst=[]
for i in range(1,n+1):
   for j in my_list:
        lst.append(j+str(i))
print(lst)
