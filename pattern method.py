

#pattern method

#n=int(input("enter the numbers:"))
#for i in range(1,n+1):
# for j in range(1,i+1):
#  print(j,end="")
# print()

#-----------------------------------------------------------------------------------------------------------------

#n = int(input("enter the numbers:"))
#for i in range(1, n + 1):
#  for j in range(1, i + 1):
#   print(i,end="")
#  print()

#-----------------------------------------------------------------------------------------------------------------

#n=int(input("enter the numbers:"))
#for i in range(1,n+1):
# for j in range(1,i+1):
#  print("*",end="")
# print()

#-----------------------------------------------------------------------------------------------------------------

#n = int(input("enter the numbers:"))
#for i in range(n,0,-1):
#    for j in range(1,i + 1):
#        print(j, end="")
#    print()

#-----------------------------------------------------------------------------------------------------------------

#n = int(input("enter the numbers:"))
#for i in range(1,n+1):
# for j in range(1,i+1):
#  print("*",end="")
# print()
#for i in range(n+1,0,-1):
#    for j in range(1, i + 1):
#        print("*", end="")
#    print()

#-----------------------------------------------------------------------------------------------------------------

#n=input("enter the string:")
#for i in range(len(n)):
# for j in range(i+1):
#  print(n[j],end="")
# print()

#----------------------------------------------------------------------------------------------------------------

num=int(input("enter the number:"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()

#------------------------------------------------------------------------------------------------------------------