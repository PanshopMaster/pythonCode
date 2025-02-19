class Guitar:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def play(self):
        return f"Playing the {self.brand} {self.model}!"

    def get_info(self):
        return f"{self.year} {self.brand} {self.model} - ${self.price}"