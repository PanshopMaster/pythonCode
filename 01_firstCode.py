# This program takes user input and prints it

# Taking input from the user
#user_input = input("Enter something: ")

# Printing the user input
#print("You entered:", user_input)

class Trabajador:
    def __init__(self, name, grad, age):
        self.name = name
        self.grad = grad
        self.age = int (age * 2)

    def mostrar_informacion(self):
        print(f"Nombre: {self.name}, Puesto: {self.grad}, Edad: {self.age}")

# Ejemplo de uso
name_t = input("Presiona Enter para continuar:")
puesto = input("Ingresa el puesto del trabajador: ")
edad = input("Ingresa la edad del trabajador: ")

trabajador1 = Trabajador(name_t, puesto , edad)
trabajador1.mostrar_informacion()