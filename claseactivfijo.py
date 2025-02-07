class ActivoFijo:
    def __init__(self, nombre, valor_inicial, vida_util, valor_residual=0):
        self.nombre = nombre
        self.valor_inicial = valor_inicial  
        self.vida_util = vida_util
        self.valor_residual = valor_residual

    def depreciacion_anual(self):
        return (self.valor_inicial - self.valor_residual) / self.vida_util

    def __str__(self):
        return f"Activo Fijo: {self.nombre}, Valor Inicial: {self.valor_inicial}, Vida Útil: {self.vida_util} años, Valor Residual: {self.valor_residual}"
    print("Activo Fijo: {0}, Valor Inicial: {1}, Vida Útil: {2} años, Valor Residual: {3}".format(nombre, valor_inicial, vida_util, valor_residual))
    class Customer:
        def __init__(self, customer_id, name, email):
            self.customer_id = customer_id
            self.name = name
            self.email = email

        def __str__(self):
            return f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}"
        