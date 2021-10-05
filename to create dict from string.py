#write a program to create dictionary from the string

string="testleaf"
dct={}
for i in string:
    dct[i]=string.count(i)
print(dct)