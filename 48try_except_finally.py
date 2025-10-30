try:
  file = open('example.txt', 'r')
  content = file.read()
except FileNotFoundError:
   print("Error: The file was not found.")
finally:
   file.close()
print("\nThis program is written and executed by Sahil Singh (0231BCA035)")
