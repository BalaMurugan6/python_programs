#create a new list which contains the element ,only starts with 'a' using filter functions

fruit=["apple","banana","guava","apricot","mango","avocados"]
lst=[]
for i in fruit:
    if i.startswith("a"):
        lst.append(i)
print(lst)

#using filter function
fruit=["apple","banana","guava","apricot","mango","avocados"]
x=list(filter(lambda f:(f.startswith("a")),fruit))
print(x)
