unit = input("Is this temperature in Celsius or Fahrenheit (C/F)?: ")
temp = float(input("What is the temperature?: "))
if unit == "C" or unit == "c":
    temp = temp * 9/5 + 32
    unit = "F"
elif unit == "F" or unit == "f":
    temp = (temp - 32) * 5/9
    unit = "C"
else:
    print(f"{unit} is an invalid unit measurement.")

print(f"The temperature is {temp:.2f}°{unit}.")

