#write a program to return longest word from the list of word

inp=['welcome','to','python','world']
length=max(map(lambda x:len(x),inp))
for i in inp:
    if length==len(i):
        print(i)

              #or
inp=['welcome','to','python','world']
lst=[]
for i in inp:
    x=len(i)
    lst.append(x)
y=max(lst)
print(y)
for i in inp:
    if y==len(i):
        print(i)

       #or
input=['welcome','to','python','world']
x=max(input,key=len)
print(x)