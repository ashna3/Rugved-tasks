#Write a python program to sort a string alphabetically and print the count of each character.

def sort_and_count(string):
    # Check if the input is a string
    if not isinstance(string, str):
        raise ValueError("Input must be a string.")

    # Remove spaces and convert to lowercase for uniformity
    string = string.replace(" ", "").lower()

    # Sort the string alphabetically
    sorted_string = ''.join(sorted(string))

    # Count the occurrences of each character
    char_count = {}
    for char in sorted_string:
        char_count[char] = char_count.get(char, 0) + 1

    # Print the sorted string
    print("Sorted string:", sorted_string)

    # Print the count of each character
    print("Character counts:")
    for char, count in char_count.items():
        print(f"{char}: {count}")

    return sorted_string, char_count

# Call the function
sort_and_count("Hello World")