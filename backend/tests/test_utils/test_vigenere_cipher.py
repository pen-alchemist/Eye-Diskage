import pytest

from backend.utils.vigenere_cipher import vigenere_cipher


def test_encrypt_uppercase():
    """Test encryption with uppercase letters."""
    assert vigenere_cipher("HELLO", "KEY") == "RIJVS"

def test_encrypt_lowercase():
    """Test encryption with lowercase letters."""
    assert vigenere_cipher("hello", "key") == "rijvs"

def test_decrypt_uppercase():
    """Test decryption with uppercase letters."""
    assert vigenere_cipher("RIJVS", "KEY", mode='decrypt') == "HELLO"

def test_decrypt_lowercase():
    """Test decryption with lowercase letters."""
    assert vigenere_cipher("rijvs", "key", mode='decrypt') == "hello"

def test_encrypt_with_non_letter_characters():
    """Test encryption with non-letter characters."""
    assert vigenere_cipher("Hello, World!", "key") == "Rijvs, Ambpb!"

def test_decrypt_with_non_letter_characters():
    """Test decryption with non-letter characters."""
    assert vigenere_cipher("Rijvs, Uyvjn!", "key", mode='decrypt') == "Hello, Qalfp!"

def test_encrypt_with_long_key():
    """Test encryption with a key longer than the text."""
    assert vigenere_cipher("HELLO", "LONGKEY") == "SSYRY"

def test_decrypt_with_long_key():
    """Test decryption with a key longer than the text."""
    assert vigenere_cipher("SSWXC", "LONGKEY", mode='decrypt') == "HEJRS"

def test_encrypt_with_short_key():
    """Test encryption with a key shorter than the text."""
    assert vigenere_cipher("HELLO", "KY") == "RCVJY"

def test_decrypt_with_short_key():
    """Test decryption with a key shorter than the text."""
    assert vigenere_cipher("RIJVS", "KY", mode='decrypt') == "HKZXI"

def test_encrypt_empty_string():
    """Test encryption with an empty string."""
    assert vigenere_cipher("", "key") == ""

def test_decrypt_empty_string():
    """Test decryption with an empty string."""
    assert vigenere_cipher("", "key", mode='decrypt') == ""

def test_encrypt_with_invalid_mode():
    """Test encryption with an invalid mode."""
    with pytest.raises(TypeError):
        vigenere_cipher(4, "key", mode='invalid_mode')

def test_decrypt_with_invalid_mode():
    """Test decryption with an invalid mode."""
    with pytest.raises(TypeError):
        vigenere_cipher("RIJVS", None, mode='invalid_mode')

def test_encrypt_with_mixed_case_key():
    """Test encryption with a mixed case key."""
    assert vigenere_cipher("HELLO", "KeY") == "RIJVS"

def test_decrypt_with_mixed_case_key():
    """Test decryption with a mixed case key."""
    assert vigenere_cipher("RIJVS", "KeY", mode='decrypt') == "HELLO"

def test_encrypt_with_mixed_case_text():
    """Test encryption with mixed case text."""
    assert vigenere_cipher("HeLlO", "key") == "RiJvS"

def test_decrypt_with_mixed_case_text():
    """Test decryption with mixed case text."""
    assert vigenere_cipher("RiJvS", "key", mode='decrypt') == "HeLlO"
