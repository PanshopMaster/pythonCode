#if = do some code only if some condition is true
#else = do some code only if the condition is false
import os

age = int(input("Enter your age: "))
if age >= 18 and age < 100:
    print("You are a aduls")
elif age < 0:
    print("You haven't been born yet")
elif age ==100:
    print("You are a centenarian")
else:
    print("You are an adult")
