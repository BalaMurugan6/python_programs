#A store has different categories of products in stock as shown below.
#Item Number= [101, 102, 103, 104]
# Item Name= [Milk, Cheese,Bread]
# Stock= [10, 20, 15, 16]  Price= [42, 50, 500, 40]
# When user give input with 2 values as -
# 1. Item number for item which user wish to buy.
# 2. Quantity for the item entered above.
# When user enters above input, the stock.
# 1. If quantity is less than stock and item is available display a notification message showing Output
# Line1- INR price in float with precision1 user while placing order, then ay message:
# Line2- LEFT stock for Item after purchase Output
# 2. If the quantity in stock is less than quantity entered by Output
# Line1- NO STOCK Output
# 3: If user enter character as input for item number and quantity or
# enter item number which is not available then display following message and stop. Output
# Line1- INVALID INPUT

item=[201,202,203,204]
cost=[55,65,75,85]
stock=[10,12,19,23]
x=int(input("Enter the item"))
y=int(input("enter the quantity"))
if x in item:
   for i in range(len(item)):
      if x==item[i]:
          if y<=stock[i]:
             print(f"the cost of item {x} is {cost[i]*y}")
             print(f"the remaining stock of {x} is {stock[i]-y}")
          else:
             print("out of stock")
else:
    print("invalid item")
