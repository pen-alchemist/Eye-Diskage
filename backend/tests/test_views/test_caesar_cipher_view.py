from django.urls import reverse

from rest_framework import status


def test_caesar_cipher_view_post_valid_encrypt_status_code(client_django):
    """Test the status code for a valid POST request for encryption."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'HELLO', 'shift': 3, 'mode': 'encrypt'})
    assert response.status_code == status.HTTP_200_OK


def test_caesar_cipher_view_post_valid_encrypt_response_data(client_django):
    """Test the response data for a valid POST request for encryption."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'HELLO', 'shift': 3, 'mode': 'encrypt'})
    assert response.json() == {"result": "KHOOR"}


def test_caesar_cipher_view_post_invalid_shift_status_code(client_django):
    """Test the status code for an invalid shift (non-integer)."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'HELLO', 'shift': 'invalid', 'mode': 'encrypt'})
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_caesar_cipher_view_post_invalid_shift_response_data(client_django):
    """Test the response data for an invalid shift (non-integer)."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'HELLO', 'shift': 'invalid', 'mode': 'encrypt'})
    assert response.json() == {"error": "Wrong shift type! invalid literal for int() with base 10: 'invalid'"}

def test_caesar_cipher_view_post_default_shift_and_mode_status_code(client_django):
    """Test the status code for a POST request with default shift and mode."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'HELLO'})
    assert response.status_code == status.HTTP_200_OK


def test_caesar_cipher_view_post_default_shift_and_mode_response_data(client_django):
    """Test the response data for a POST request with default shift and mode."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'HELLO'})
    assert response.json() == {"result": "KHOOR"}  # Default shift is 3 and mode is 'encrypt'


def test_caesar_cipher_view_post_text_size_exceeds_limit_status_code(client_django):
    """Test the status code for a POST request with text size exceeding the limit."""
    url = reverse('eye-caesar-text')
    large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
    response = client_django.post(url, data={'text': large_text, 'shift': 3, 'mode': 'encrypt'})
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_caesar_cipher_view_post_valid_decrypt_status_code(client_django):
    """Test the status code for a valid POST request for decryption."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'KHOOR', 'shift': 3, 'mode': 'decrypt'})
    assert response.status_code == status.HTTP_200_OK


def test_caesar_cipher_view_post_valid_decrypt_response_data(client_django):
    """Test the response data for a valid POST request for decryption."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'KHOOR', 'shift': 3, 'mode': 'decrypt'})
    assert response.json() == {"result": "HELLO"}


def test_caesar_cipher_view_post_empty_text_status_code(client_django):
    """Test the status code for a POST request with empty text."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': '', 'shift': 3, 'mode': 'encrypt'})
    assert response.status_code == status.HTTP_200_OK


def test_caesar_cipher_view_post_empty_text_response_data(client_django):
    """Test the response data for a POST request with empty text."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': '', 'shift': 3, 'mode': 'encrypt'})
    assert response.json() == {"result": ""}


def test_caesar_cipher_view_post_negative_shift_status_code(client_django):
    """Test the status code for a POST request with negative shift."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'HELLO', 'shift': -3, 'mode': 'encrypt'})
    assert response.status_code == status.HTTP_200_OK

def test_caesar_cipher_view_post_negative_shift_response_data(client_django):
    """Test the response data for a POST request with negative shift."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'HELLO', 'shift': -3, 'mode': 'encrypt'})
    assert response.json() == {"result": "EBIIL"}


def test_caesar_cipher_view_post_large_shift_status_code(client_django):
    """Test the status code for a POST request with a shift larger than 26."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'HELLO', 'shift': 29, 'mode': 'encrypt'})
    assert response.status_code == status.HTTP_200_OK


def test_caesar_cipher_view_post_large_shift_response_data(client_django):
    """Test the response data for a POST request with a shift larger than 26."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'HELLO', 'shift': 29, 'mode': 'encrypt'})
    assert response.json() == {"result": "KHOOR"}


def test_caesar_cipher_view_post_non_alphabetic_characters_status_code(client_django):
    """Test the status code for a POST request with non-alphabetic characters."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'HELLO 123!', 'shift': 3, 'mode': 'encrypt'})
    assert response.status_code == status.HTTP_200_OK


def test_caesar_cipher_view_post_non_alphabetic_characters_response_data(client_django):
    """Test the response data for a POST request with non-alphabetic characters."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'HELLO 123!', 'shift': 3, 'mode': 'encrypt'})
    assert response.json() == {"result": "KHOOR 123!"}


def test_caesar_cipher_view_post_missing_text_status_code(client_django):
    """Test the status code for a POST request with missing text."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'shift': 3, 'mode': 'encrypt'})
    assert response.status_code == status.HTTP_200_OK


def test_caesar_cipher_view_post_missing_text_response_data(client_django):
    """Test the response data for a POST request with missing text."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'shift': 3, 'mode': 'encrypt'})
    assert response.json() == {'result': ''}


def test_caesar_cipher_view_post_invalid_mode_status_code(client_django):
    """Test the status code for a POST request with invalid mode."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'HELLO', 'shift': 3, 'mode': 'invalid'})
    assert response.status_code == status.HTTP_200_OK


def test_caesar_cipher_view_post_invalid_mode_response_data(client_django):
    """Test the response data for a POST request with invalid mode."""
    url = reverse('eye-caesar-text')
    response = client_django.post(url, data={'text': 'HELLO', 'shift': 3, 'mode': 'invalid'})
    assert response.json() == {'result': 'KHOOR'}
