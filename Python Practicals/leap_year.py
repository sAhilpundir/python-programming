year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

print("\nThis program is written and executed by Sahil Singh (0231BCA035)")
