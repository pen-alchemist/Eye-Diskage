def vigenere_cipher(text, key, mode='encrypt'):
    """
    Encrypts or decrypts a text using the Vigenère cipher.

    :param text: The input text to be encrypted or decrypted.
    :param key: The key used for encryption or decryption.
    :param mode: 'encrypt' or 'decrypt' (default is 'encrypt').
    :return: The encrypted or decrypted text.
    """
    result = ""

    # Determine the shift direction based on the mode
    if mode == 'decrypt':
        key_shift = -1
    else:
        key_shift = 1

    # Repeat the key to match the length of the text
    key_repeated = (key * (len(text) // len(key) + 1))[:len(text)]

    # Iterate over each character in the text
    for i, char in enumerate(text):
        # Check if the character is an uppercase letter
        if char.isupper():
            # Calculate the shift based on the corresponding key character
            shift = (ord(key_repeated[i].upper()) - 65) * key_shift
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            # Calculate the shift based on the corresponding key character
            shift = (ord(key_repeated[i].lower()) - 97) * key_shift
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, leave it unchanged
            result += char

    return result
