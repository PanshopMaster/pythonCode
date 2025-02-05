# 2 Shopping Cart program 
items = input("What items would you like to buy: ")
prices = float(input("What is the price?: "))
qty = input("How many would you like to buy?: ")

total = prices * int(qty)
print(f"Your total is: {total}")
print(f"Thank you for shopping with us, you have purchased {qty} X {items} at {prices} each for a total of {total}")