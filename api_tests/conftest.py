import pytest

from django.test import RequestFactory

@pytest.fixture(scope="session")
def rf():
    """Django RequestFactory instance for creating mock requests."""
    return RequestFactory()


@pytest.fixture(scope="session")
def api_endpoints():
    """Centralized API endpoint URLs."""
    return {
        "caesar_cipher": "/api/eye_diskage/caesar-cipher/",
        "django_ker_generate": "/api/eye_diskage/django-ker-generate/",
        "secure_random_numbers": "/api/eye_diskage/secure-random-numbers/",
        "vigenere_cipher": "/api/eye_diskage/vigenere-cipher/",
    }


@pytest.fixture(scope="function")
def valid_encrypt_data():
    """Valid payload for encryption requests."""
    return {'text': 'HELLO', 'key': 'KEY', 'mode': 'encrypt'}


@pytest.fixture(scope="function")
def valid_decrypt_data():
    """Valid payload for decryption requests."""
    return {'text': 'RIJVS', 'key': 'KEY', 'mode': 'decrypt'}
