#sum of digits
num=1456
sum_num=0
while num>0:
    digit=num%10
    sum_num=sum_num+digit
    num=num//10
print(sum_num)

#using recursion
def sod(n):
    if n==0:
        return 0
    else:
        return n%10+sod(n//10)
n=int(input("Enter the number"))
print(sod(n))