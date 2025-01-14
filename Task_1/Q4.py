#Write a python function to perform selection sort on a given string.

def selection_sort_string(s):
    # Convert the string to a list of characters
    char_list = list(s)

    # Get the length of the list
    n = len(char_list)

    # Iterate over each character in the list
    for i in range(n):
        # Assume the current index is the minimum
        min_index = i

        # Find the index of the smallest character in the remaining unsorted part of the list
        for j in range(i + 1, n):
            if char_list[j] < char_list[min_index]:
                min_index = j

        # Swap the found minimum element with the first element
        char_list[i], char_list[min_index] = char_list[min_index], char_list[i]

    # Convert the list of characters back to a string
    return ''.join(char_list)

# Call the function and print the output
sorted_string = selection_sort_string("hello")
print(sorted_string)  # Output: "ehllo"

