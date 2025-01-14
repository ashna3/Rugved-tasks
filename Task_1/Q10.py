def is_valid_credit_card(card_number):
    # Convert the card number to a string and remove spaces
    card_number = card_number.replace(" ", "")

    # Check if the card number consists only of digits
    if not card_number.isdigit():
        return False

    # Reverse the card number for processing
    reversed_digits = [int(digit) for digit in card_number][::-1]

    # Apply Luhn's algorithm
    total = 0
    for i, digit in enumerate(reversed_digits):
        # Double every second digit
        if i % 2 == 1:
            digit *= 2
            # If doubling results in a number > 9, subtract 9
            if digit > 9:
                digit -= 9
        total += digit

    # A valid credit card number will have a total that is a multiple of 10
    return total % 10 == 0


# Example usage
card_number = input("Enter the credit card number: ")
if is_valid_credit_card(card_number):
    print("The credit card number is valid.")
else:
    print("The credit card number is not valid.")