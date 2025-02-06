import time
class ActivoFijo:
    def __init__(self, nombre, valor, depreciacion_anual):
        self.nombre = nombre
        self.valor = valor
        self.depreciacion_anual = depreciacion_anual

    def calcular_valor_actual(self, anios):
        valor_actual = self.valor * ((1 - self.depreciacion_anual) ** anios)
        return valor_actual

# Example usage
producto = input("Ingrese el nombre del activo: ")
valor = int(input("Ingrese el valor del activo: "))
depreciacion = float(input("Ingrese la depreciación anual: "))
activo = ActivoFijo(producto, valor, depreciacion)
print(f"El valor actual del activo {activo.nombre} después de 3 años es: {activo.calcular_valor_actual(3)}")