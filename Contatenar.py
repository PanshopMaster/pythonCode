import os
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total = (bill + bill * tip / 100) / people
print(f"Total Bill: ${bill:.2f}")
print(f"Tip {tip}%: ${bill * tip / 100:.2f}")
print(f"Each person should pay: ${total:.2f}")
os.system("pause")
