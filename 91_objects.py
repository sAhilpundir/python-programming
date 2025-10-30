#Q91. Define a class with objects

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

print("\nThis program is written and executed by Sahil Singh (0231BCA035)")
