# Remove vowels in a given string

x="Bala"
v=["a","e","i","o","u"]
y=""
for i in x:
    if i.lower() not in v:
        y=y+i
print(y)