#Python convert pulgadas centimetros

medida = float(input("Ingrese la medida: "))
unit = input("Ingrese la unidad de medida (C)m o (I)n: ")
if unit == "C" or unit == "c":
    medida = medida * 2.54
    unit = "in"
elif unit == "I" or unit == "i":
    medida = medida / 2.54
    unit = "cm"
else:
    print(f"Unidad no valida{unit}")
print(f"La medida en centimetro es: {medida:.2f}{unit}") 