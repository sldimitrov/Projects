current_year = 2025

class Car:

    def __init__(self, brand, fuel, model, year):
        self.brand = brand
        self.fuel = fuel
        self.model = model
        self.year = year

    def re_fuel(self):
        if self.fuel < 100:
            self.fuel = 100

    def change_brand(self, brand):
        self.brand = brand

    def change_model(self, model):
        self.model = model

    def get_age(self):
        return current_year - self.year

    def __str__(self):
        return f"{self.brand} - {self.fuel} - {self.model}"

car1 = Car('Mercedes', "100", "cabriolet", 2020)

print(car1.get_age())
