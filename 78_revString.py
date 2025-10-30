#Q78. reverse a string without a predefined function

def stringReverse(s):
    rs=" "
    for char in s:
        rs=char+rs
    print(rs)
stringReverse(input("Enter a string: "))

print("\nThis program is written and executed by Sahil Singh (0231BCA035)")
