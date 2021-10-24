#write a code for print each character count for given string (using library method)
string="testleaf"
dct={}
for i in string:
    dct[i]=string.count(i)
print(dct)

#without using library method
input="testleaf"
dict={}
for i in input:
    dict[i]=dict.get(i,0)+1
print(dict)
           #or
input1="testleaf"
dic={}
for i in input1:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
print(dic)
