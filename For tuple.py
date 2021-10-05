
#For tuple
#write a program which accepts a sequence of comma-seperated numbers from console and generate a list and a tuple
input=input("enter the number")
list=[]
for i in input.split(","):
    list.append(i)
print(list)
print(tuple(list))

#Write a program to generate and print another tuple whose values are even numbers in a given tuple
input=(1,2,3,4,5,6,7,8,10)
even_num=[]
for i in input:
    if(i%2)==0:
        even_num.append(i)
print(tuple(even_num))
