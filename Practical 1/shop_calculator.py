# Shop_Calculator
total = 0
number = int(input("number of items: "))
"""
price of item 1: 100
price of item 2: 35.56
price of item 3: 3.24
"""
while number < 0:
    print("invalid number of items")
    number = int(input("number of items: "))

for i in range(number):
    price = float(input("price of item:"))
    total += price
if total > 100:
    total = total * 0.9
print("Total price for {} items is ${:.2f}".format(number, total))