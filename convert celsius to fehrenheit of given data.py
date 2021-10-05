#write a program to convert celsius to fehrenheit of given data

#using list comprehension method
data={'chennai':29,'bangalore':36,'hyderabad':19,'delhi':27}
x=dict([(i[0],(9/5)*i[1]+32) for i in data.items()])
print(x)

#using lambda
x=map(lambda d:(d[0],(9/5)*d[1]+32),data.items())
print(dict(x))