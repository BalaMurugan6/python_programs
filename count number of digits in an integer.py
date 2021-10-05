#using inbuilt methods
num=12345
print(len(str(num)))

#using while loop
num=12345
count=0
while num>0:
    num=num//10
    count=count+1
print(count)
