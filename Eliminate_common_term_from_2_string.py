
#Eliminate common term from two strings

str1="hellow bala"
str2="how r u bala"
a=set(str1.split())
b=set(str2.split())
common=a.intersection(b)
def remove(x):
    lst=[]
    for i in x.split():
        if i not in common:
            lst.append(i)
    return (" ".join(lst))
print(remove(str1))
print(remove(str2))