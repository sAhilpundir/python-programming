def fibonacci(n):
 a, b = 0, 1
 while a < n:
  yield a
 a, b = b, a + b
for num in fibonacci(10):
 print(num) 
print("\nThis program is written and executed by Sahil Singh (0231BCA035)")
