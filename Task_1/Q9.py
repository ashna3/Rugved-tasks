def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Shift within the bounds of the alphabet
            shift_base = ord('a') if char.islower() else ord('A')
            # Calculate the new shifted character
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_text += char

    return encrypted_text


# Example usage
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value (1-25): "))
encrypted = caesar_cipher_encrypt(text, shift)
print("Encrypted text:", encrypted)