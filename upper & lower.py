
#using lower and upper
#input="WeLcome to My woRlD"
#for i in input:
#    if(i.isupper()):
#        print(i.lower(),end="")
#    else:
#        print(i.upper(),end="")

#without using library functions
                                                                     #ascii value
inp="WeLcome"                                                        #A---------65
for i in inp:                                                        #a---------97
    if ord(i)<97:
        print(chr(ord(i)+32),end="")
    else:
        print(chr(ord(i)-32),end="")

#using lambda function

#input="WeLcome to zt"
#x=list(map(lambda a:(a.upper()) if(a.islower()) else a,input))
#y="".join(x)
#print(y)


