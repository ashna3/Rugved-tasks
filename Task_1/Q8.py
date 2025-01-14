# Write a python program to divide a given string into equal parts containing n(user input) characters of same sequence.

def divide_string(s, n):
    # Check if the string can be divided into equal parts of size n
    if len(s) % n != 0:
        return f"Cannot divide the string into equal parts of {n} characters."

    # Initialize an empty list to hold the parts
    parts = []

    # Iterate over the string and divide it into parts
    for i in range(0, len(s), n):
        # Extract the part from the string
        part = s[i:i + n]
        # Add the part to the list of parts
        parts.append(part)

    return parts


# Main program
if __name__ == "__main__":
    # Get the string to be divided from the user
    s = input("Enter the string to be divided: ")
    # Get the number of characters per part from the user
    n = int(input("Enter the number of characters per part: "))

    # Divide the string and store the result
    result = divide_string(s, n)

    if isinstance(result, str):
        # If the result is a string, print the error message
        print(result)
    else:
        # If the result is a list, print each part separately
        print("Divided string into equal parts:")
        for part in result:
            print(part)


