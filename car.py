class Car:
    def __init__(self, make, model,color, year):
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    def get_description(self):
        return f"{self.year} {self.make} {self.model}{self.color}"

    def start_engine(self):
        return "The engine is now running."

    def stop_engine(self):
        return "The engine is now off."
