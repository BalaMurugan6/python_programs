#using library methods
st="bala$murugan"
st1=st.replace("$","")
print(st1)

#without using library methods
x="bala$murugan ramesh"
y=""
for i in x:
    if i!="$":
        y=y+i
print(y)
