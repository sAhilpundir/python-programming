from datetime import date

birth_year = int(input("Enter birth year: "))
birth_month = int(input("Enter birth month: "))
birth_day = int(input("Enter birth day: "))

today = date.today()
age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
print("Your age is:", age)
print("\nThis program is written and executed by Sahil Singh (0231BCA035)")