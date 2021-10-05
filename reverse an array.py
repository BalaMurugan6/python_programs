#using reverse in-built method
lst=[1,7,5,8,9]
print(list(reversed(lst)))

#using reverse without using in-built method
lst1=[1,7,5,8,9]
for i in range(len(lst1)-1,-1,-1):
    print(lst1[i],end=" ")