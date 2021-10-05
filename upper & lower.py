
#using lower and upper
input="WeLcome to My woRlD"
for i in input:
    if(i.isupper()):
        print(i.lower(),end="")
    else:
        print(i.upper(),end="")

#using chr(ord())

#input="WeLcome"
#for i in input:
#    if(i.isupper()):
#        print(chr(ord(i)+32),end="")
#    else:
#        print(chr(ord(i)-32),end="")

#using lambda function

#input="WeLcome to zt"
#x=list(map(lambda a:(a.upper()) if(a.islower()) else a,input))
#y="".join(x)
#print(y)


