#Create a function that checks whether given string is an anagram or not?

def are_anagrams(str1, str2):
    # Remove any spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # If the lengths of the strings are different, they cannot be anagrams
    if len(str1) != len(str2):
        return False

    # Sort the characters of both strings and compare them
    return sorted(str1) == sorted(str2)

# Example input
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')