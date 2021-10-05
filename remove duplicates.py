#remove duplicates using set
x=[5,9,4,5,3,3,1]
print(set(x))                         #output is unordered


#remove duplicates with same order
n=[5,9,4,5,3,3,1]
lst=[]
for i in n:
    if i not in lst:
        lst.append(i)
print(lst)