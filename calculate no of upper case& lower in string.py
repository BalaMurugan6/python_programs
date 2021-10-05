#calculate number of uppercase letters and lowercase letters in a given string
string="The quick Brow Fox"
uppercase=0
lowercase=0
for i in string:
    if i.isupper():
        uppercase=uppercase+1
    if i.islower():
        lowercase=lowercase+1
print("No of uppercases in the string:",uppercase)
print("No of lowercases in the string:",lowercase)