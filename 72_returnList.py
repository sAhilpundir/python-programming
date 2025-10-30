#Q72. Returning a List or Dictionary

def get_squares(numbers):
    squares = [n ** 2 for n in numbers]
    return squares
nums = [1, 2, 3, 4]
squares_list = get_squares(nums)
print(squares_list)
print("\nThis program is written and executed by Sahil Singh (0231BCA035)")
