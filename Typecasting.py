#Typecasting = the process of  a variable from data type to another data type 
# str() = converts any data type into a string data type
# int() = converts any data type into a integer data type
# float() = converts any data type into a float data type
# bool() = converts any data type into a boolean data type

name = ""
age = 22
gpa = 3.5
is_student = True

name = bool(name)
if name == True:
    print("Hello")
else:
    print("Goodbye")