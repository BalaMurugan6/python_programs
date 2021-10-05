#Create a program to add even number as a seperate set from the exist set
st={23,512,24,75,46,91}
sum=0
lst=[]
for i in st:
    if(i%2)==0:
       lst.append(i)
       sum=sum+i
print(set(lst))
print(sum)

