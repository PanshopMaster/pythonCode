# Python weight converter
weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit== "K":
    weight = weight * 2.20462
    unit = "Lbs"
elif unit == "L":
    weight = weight / 2.20462
    unit = "Kgs"
else:
    print(f"{unit}Invalid input")

print(f"you Weight is: {weight} {unit}")

