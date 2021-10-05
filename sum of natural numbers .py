#sum of natural numbers upto num
num=15
if num<0:
    print("please enter positive number")
else:
    sum=0
    while num>0:
        sum=sum+num
        num=num-1
    print("the sum is",sum)

                 #or
g = 15
sum = 0
for i in range(1, g + 1):
    sum = sum + i
print(sum)


#using recursion
def find_sum(n):
    if n==1:
        return 1
    else:
        return n+find_sum(n-1)
n=int(input("enter the number"))
print(find_sum(n))







