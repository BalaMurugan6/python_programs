punctuation="""!#$%^&_*()\|{}[]"'-/?.,:;"""
x="Hellow!,he said--and went."
no_punc=""
for char in x:
    if char not in punctuation:
        no_punc=no_punc+char
print(no_punc)


#i/p--->Welcome to ideas2it  o/p----->Welcome ideas2it

#input="Welcome to ideas2it"
#for i in input.split(" "):
#    if i=="to":
#        continue
#    print(i,end=" ")

    #or

input="Welcome to ideas2it"
x="to"
lst=[]
for i in input.split():
    if i not in x:
        lst.append(i)
print(" ".join(lst))


#Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

#for fizzbuzz in range(51):
#    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#        print("fizzbuzz")
#        continue
#    elif fizzbuzz % 3 == 0:
#        print("fizz")
#        continue
#    elif fizzbuzz % 5 == 0:
#        print("buzz")
#        continue
#    print(fizzbuzz)

#Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

x="green-red-yellow-black-white"
items=[i for i in x.split("-")]
items.sort()
print("-".join(items))

           #or

items="green-red-yellow-black"
lst=[]
for i in items.split('-'):
    lst.append(i)
x=sorted(lst)
print("-".join(x))

#------------------------------------------------------------------------------------------------------
x="a3b2c1"
output=""
for i in x:
    if i.isalpha():
        temp=i
    else:
        d=int(i)
        output=output+temp*d
print(output)

