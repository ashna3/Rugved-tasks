def coleman_liau_index(text):
    # Initialize counters
    letters = sum(c.isalpha() for c in text)
    words = len(text.split())
    sentences = sum(c in '.!?' for c in text)

    # Calculate L and S
    L = (letters / words) * 100 if words > 0 else 0
    S = (sentences / words) * 100 if words > 0 else 0

    # Calculate the index
    index = 0.0588 * L - 0.296 * S - 15.8

    # Round to the nearest integer
    grade_level = round(index)

    # Return grade level
    if grade_level < 1:
        return "Before Grade 1"
    elif grade_level >= 16:
        return "Grade 16+"
    else:
        return f"Grade {grade_level}"


# Example usage
text = input("Enter the text to analyze: ")
grade_level = coleman_liau_index(text)
print(grade_level)
