#to check if a year is leap year or not
year=1600
if (year%4==0 and year%100!=0) or year%400==0:
    print(year,"is the leap year")
else:
    print(year,"is not a leap year")