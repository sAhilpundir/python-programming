

class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
# Demonstrating polymorphism
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

print("\nThis program is written and executed by Sahil Singh (0231BCA035)")
