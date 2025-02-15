import pytest

from django.test import RequestFactory


@pytest.fixture
def rf():
    return RequestFactory()

@pytest.fixture
def caesar_cipher_url():
    return "/api/eye_diskage/caesar-cipher/"

@pytest.fixture
def caesar_cipher_url():
    return "/api/eye_diskage/django-ker-generate/"

@pytest.fixture
def secure_random_numbers_url():
    return "/api/eye_diskage/secure-random-numbers/"

@pytest.fixture
def vigenere_cipher_url():
    return "/api/eye_diskage/vigenere-cipher/"

@pytest.fixture
def valid_encrypt_data():
    return {'text': 'HELLO', 'key': 'KEY', 'mode': 'encrypt'}

@pytest.fixture
def valid_decrypt_data():
    return {'text': 'RIJVS', 'key': 'KEY', 'mode': 'decrypt'}
