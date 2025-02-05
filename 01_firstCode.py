# This program takes user input and prints it

# Taking input from the user
#user_input = input("Enter something: ")

# Printing the user input
#print("You entered:", user_input)

class Trabajador:
    def __init__(self, name, grad, age):
        self.name = name
        self.grad = grad
        self.age = age

    def mostrar_informacion(self):
        print(f"Nombre: {self.name}, Puesto: {self.grad}, Edad: {self.age}")

# Ejemplo de uso
input

trabajador1 = Trabajador("Juan", "Ingeniero", "22")
trabajador1.mostrar_informacion()