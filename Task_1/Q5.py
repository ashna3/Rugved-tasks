# Find the factorial of a given number using recursion.

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: factorial of n is n times factorial of (n-1)
        return n * factorial(n - 1)

# Get user input
user_input = input("Enter a number to compute factorial: ")

# Validate and process the input
try:
    number = int(user_input)  # Convert input to an integer
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(number)  # Factorial of number
        print(f"The factorial of {number} is {result}.")  # Print the result
except ValueError:
    print("Please enter a valid integer.")
