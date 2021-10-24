#Write a python program that accepts a word from the user and reverse it using for loop
#(reverse a word)
word=input("enter the word")
str1=""
for i in word:
    str1=i+str1
print(str1)
                          #or
#word="fghjk"
#print(word[::-1]

#str="bala"
#print(str[len(str)-1::-1])

#(reverse a sentence)
a="bala is a good person"
b=""
for i in a.split():
    b=i+" "+b
print(b)
