#count no of even & odd number
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
counteven=0
countodd=0
for i in numbers:
    if i%2==0:
        counteven=counteven+1
    else:
        countodd=countodd+1
print("even no:",counteven)
print("odd no:",countodd)