#Using a Temporary Variable
a, b, c = 1, 2, 3

temp = a
a = b
b = c
c = temp

print("a =", a, "b =", b, "c =", c)

#Using Addition & Subtraction
a, b, c = 1, 2, 3

a = a + b + c   # a = 6
b = a - (b + c) # b = 1
c = a - (b + c) # c = 2
a = a - (b + c) # a = 3

print("a =", a, "b =", b, "c =", c)

#Using Tuple Unpacking 
a, b, c = 1, 2, 3

a, b, c = b, c, a

print("a =", a, "b =", b, "c =", c)

print("\nThis program is written and executed by Sahil Singh (0231BCA035)")
