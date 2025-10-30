def count_up_to(max):
 count = 1
 while count <= max:
  yield count
 count += 1
for num in count_up_to(5):
 print(num) 
print("\nThis program is written and executed by Sahil Singh (0231BCA035)")
