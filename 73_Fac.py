#Q73. Factorial of a number simple func

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Taking input from user
num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")

print("\nThis program is written and executed by Sahil Singh (0231BCA035)")
