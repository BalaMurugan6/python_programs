#to check amstrong number to the given number
num=int(input("enter the number"))
temp=num
sum=0
n=len(str(num))
while temp>0:
    digit=temp%10
    sum=sum+(digit**n)
    temp=temp//10
if num==sum:
    print(num,"is a amstrong number")
else:
    print(num,"is not a amstrong number")

#to check amstrong number for a given range
#x=int(input("enter the range"))
#for num in range(x):
#    temp=num
#    sum=0
#    n=len(str(num))
#    while temp>0:
#        digit=temp%10
#        sum=sum+(digit**n)
#        temp=temp//10
#    if num==sum:
#       print(num,"is a amstrong number")
#    else:
#       print(num,"is not a amstrong number")

