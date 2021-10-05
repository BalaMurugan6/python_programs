#to find which number occurs in maximum times in a given list

list=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
x=max(list,key=list.count)
print(x)
             #or

#print the letter that occur max no of times in the last word of sentences
x="how are you mr.balamurugan"
y=x.split(" ")
print(max(y[-1],key=y[-1].count))