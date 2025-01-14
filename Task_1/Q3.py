#Write a python program to check if given number is a hill number.

def is_palindrome(value):
    # Convert the input value to a string
    str_val = str(value)
    # Check if the string is the same forwards and backwards
    return str_val == str_val[::-1]


def is_increasing_upto_middle(number):
    # Convert the number to a string
    str_num = str(number)
    # Calculate the middle index of the string
    middle_index = len(str_num) // 2

    # Check if each digit up to the middle is increasing
    for i in range(1, middle_index + 1):
        # If any digit is not greater than the previous one, return False
        if str_num[i] <= str_num[i - 1]:
            return False
    return True


def is_hill_number(number):
    # A number is a hill number if it is a palindrome and
    # the digits up to the middle are increasing
    return is_palindrome(number) and is_increasing_upto_middle(number)


def check_hill_number(number):
    # Check if the number is a hill number and print the result
    if is_hill_number(number):
        print(f"{number} is a hill number.")
    else:
        print(f"{number} is not a hill number.")

# Get user input
user_input = input("Enter a number to check if it's a hill number: ")

# Validate and process the input
try:
    number = int(user_input)  # Convert input to an integer
    check_hill_number(number)  # Check if the number is a hill number
except ValueError:
    print("Please enter a valid integer.")








