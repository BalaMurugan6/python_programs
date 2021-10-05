
#to print all prime number
lower=int(input("enter the lower interval"))
upper=int(input("enter the upper interval"))
print("prime numbers between",upper,"and",lower,"are")
for i in range (lower,upper+1):
    if i>1:
        for x in range(2,i):
            if (i%x)==0:
                break
        else:
            print(i)