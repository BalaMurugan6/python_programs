#sorting

a={23,512,24,75,46,91}
b=list(a)
print(sorted(b))

#sorted without using inbuilt sort method (bubble sort method)
arr=[23,512,24,75,46,91]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            arr[i],arr[j]=arr[j],arr[i]
print(arr)
                  #or
input=[23,512,24,6,75,91]
for i in range(0,len(input)):
    for j in range(i+1,len(input)):
        if(input[i]>input[j]):
            temp=input[i]
            input[i]=input[j]
            input[j]=temp
print(input)


