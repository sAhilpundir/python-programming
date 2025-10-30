n = int(input("Enter number: "))
sum_div = sum([i for i in range(1, n) if n % i == 0])
if sum_div == n:
    print("Perfect number")
else:
    print("Not a perfect number")
print("\nThis program is written and executed by Sahil Singh (0231BCA035)")