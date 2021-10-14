list=[34,78,5,7,92]
x=int(input("enter the number"))
if x in list:
    for i in range(len(list)):
        if list[i]==x:
            print(f"the number {x} is available in the position {i+1}")
else:
    print(f"given element {x} doesn't occur")
