

class NegativeValueError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def check_positive(value):
    if value < 0:
        raise NegativeValueError("Value cannot be negative.")
try:
    check_positive(-10)

except NegativeValueError as e:
    print(f"Custom error: {e}")

print("\nThis program is written and executed by Sahil Singh (0231BCA035)")
