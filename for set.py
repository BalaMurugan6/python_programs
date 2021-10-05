#for set
#Write a program to print this list after removing all duplicates value with original order reserved
input=[12,24,35,24,88,155,88,120,155]
x=set(input)
y=list(x)
y.sort()
print(y)

#write a program to make a list whose elements are intersection of the above given lists

a=[1,3,6,78,35,55]
b=[12,24,35,24,88,120,155]
x=set(a)
y=set(b)
x.intersection_update(y)
print(list(x))

#Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

color_list_1 ={"White", "Black", "Red"}
color_list_2 ={"Red", "Green"}

print(color_list_1.difference(color_list_2))

#Write a Python program to find the elements in a given set that are not in another set

sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("Difference of sn1 and sn2 using difference():")
print(sn1.difference(sn2))
print("Difference of sn2 and sn1 using difference():")
print(sn2.difference(sn1))
print("Difference of sn1 and sn2 using - operator:")
print(sn1-sn2)
print("Difference of sn2 and sn1 using - operator:")
print(sn2-sn1)