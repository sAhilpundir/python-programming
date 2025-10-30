

class MyClass:
    def __init__(self, value):
        self.value = value
obj = MyClass(10)

print(obj.value) # Output: 10
del obj # Decrease reference count to 00, object is destroyed, object is destroyed

print("\nThis program is written and executed by Sahil Singh (0231BCA035)")
