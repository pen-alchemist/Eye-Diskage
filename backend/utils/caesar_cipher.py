def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts a text using the Caesar cipher.

    :param text: The input text to be encrypted or decrypted.
    :param shift: The number of positions to shift each character.
    :param mode: 'encrypt' or 'decrypt' (default is 'encrypt').
    :return: The encrypted or decrypted text.
    """
    result = ""

    # Determine the shift direction based on the mode
    if mode == 'decrypt':
        shift = -shift

    # Iterate over each character in the text
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, leave it unchanged
            result += char

    return result
