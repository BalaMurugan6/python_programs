#An unsorted array which has to contain even number in even no of times and odd number in odd number of times.
#Find out the number which doesn't match
input=(6,1,4,5,4,1,6,1,6,5,6)
dt={}
for i in input:
    dt[i]=input.count(i)
print(dt)
for i in dt:
    if (i%2==0)and(dt[i]%2!=0):
        print(i)
    elif (i%2==1)and(dt[i]%2!=1):
        print(i)

#an array which may contain duplicate numbers.if the number is duplicated then it has to be present in paired no.of
#times like 2 times,4 times, 6 times.Find the unpair duplicate number in an unsorted array?
lst=[6,1,7,4,4,1,6,4]
dt={}
for i in lst:
    dt[i]=lst.count(i)
print(dt)
for i in dt:
    if (dt[i]!=2)and(dt[i]!=4)and(dt[i]!=6)and(dt[i]!=1):
        print(i)

#Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last.
# You can only swap elements of the array.
#For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
# it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B']

input=['G','B','R','R','B','R','G']
for i in range (len(input)):
     for j in range(i+1,len(input)):
          if input[i]<input[j]:
                     temp=input[i]
                     input[i]=input[j]
                     input[j]=temp
print(input)


