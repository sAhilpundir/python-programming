try:
   number = int(input("Enter a number: "))
   result = 10 / number
except ZeroDivisionError:
   print("Error: Cannot divide by zero.")
except ValueError:
   print("Error: Invalid input, Enter a valid number.")
print("\nThis program is written and executed by Sahil Singh (0231BCA035)")
