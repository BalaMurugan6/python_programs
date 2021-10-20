#input="monitor 132 cpu 234"
#output="132 monitor cpu 234"
s="monitor 132 cpu 234"
a=s.split()
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]=="132":
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(" ".join(a))


