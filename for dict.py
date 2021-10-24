#for dictionary
#write a program to generate a dictionary that contains (i,i*i)such an integral number between 1 and n and then the program should be print in dictionary
input=8
dict={}
for i in range(1,9):
    dict[i]=i*i
print(dict)

#write a program for get given character count for given string
a="testleaf"
b="e"
count=0
dict={}
for i in a:
    if(i==b):
        count=count+1
        dict["e"]=count
print(dict)

#write a code for print each word count for given string
input="Data Hellow Data"
dict={}
for i in input.split(" "):
    dict[i]=dict.get(i,0)+1
print(dict)

#writa a code for print last word count given string
t="Data Hellow Data"
h=t.split(" ")
print(str(len(h[-1])))
