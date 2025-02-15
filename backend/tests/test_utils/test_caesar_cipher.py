import pytest

from backend.utils.caesar_cipher import caesar_cipher


def test_encrypt_uppercase():
    """Test encryption with uppercase letters."""
    assert caesar_cipher("HELLO", 3) == "KHOOR"

def test_encrypt_lowercase():
    """Test encryption with lowercase letters."""
    assert caesar_cipher("hello", 3) == "khoor"

def test_decrypt_uppercase():
    """Test decryption with uppercase letters."""
    assert caesar_cipher("KHOOR", 3, mode='decrypt') == "HELLO"

def test_decrypt_lowercase():
    """Test decryption with lowercase letters."""
    assert caesar_cipher("khoor", 3, mode='decrypt') == "hello"

def test_encrypt_with_non_letter_characters():
    """Test encryption with non-letter characters."""
    assert caesar_cipher("Hello, World!", 3) == "Khoor, Zruog!"

def test_decrypt_with_non_letter_characters():
    """Test decryption with non-letter characters."""
    assert caesar_cipher("Khoor, Zruog!", 3, mode='decrypt') == "Hello, World!"

def test_encrypt_with_large_shift():
    """Test encryption with a shift larger than 26."""
    assert caesar_cipher("HELLO", 30) == "LIPPS"

def test_decrypt_with_large_shift():
    """Test decryption with a shift larger than 26."""
    assert caesar_cipher("LIPPS", 30, mode='decrypt') == "HELLO"

def test_encrypt_with_negative_shift():
    """Test encryption with a negative shift."""
    assert caesar_cipher("HELLO", -3) == "EBIIL"

def test_decrypt_with_negative_shift():
    """Test decryption with a negative shift."""
    assert caesar_cipher("EBIIL", -3, mode='decrypt') == "HELLO"

def test_encrypt_empty_string():
    """Test encryption with an empty string."""
    assert caesar_cipher("", 3) == ""

def test_decrypt_empty_string():
    """Test decryption with an empty string."""
    assert caesar_cipher("", 3, mode='decrypt') == ""

def test_encrypt_with_zero_shift():
    """Test encryption with a shift of 0."""
    assert caesar_cipher("HELLO", 0) == "HELLO"

def test_decrypt_with_zero_shift():
    """Test decryption with a shift of 0."""
    assert caesar_cipher("HELLO", 0, mode='decrypt') == "HELLO"

def test_encrypt_with_invalid_mode():
    """Test encryption with an invalid mode."""
    with pytest.raises(ValueError):
        caesar_cipher("HELLO", 3, mode='invalid_mode')

def test_decrypt_with_invalid_mode():
    """Test decryption with an invalid mode."""
    with pytest.raises(ValueError):
        caesar_cipher("KHOOR", 3, mode='invalid_mode')
