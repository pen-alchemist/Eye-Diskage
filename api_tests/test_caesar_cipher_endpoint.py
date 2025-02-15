import json
import pytest

from django.core.exceptions import RequestDataTooBig

from rest_framework import status

from backend.views import caesar_cipher_view


def test_caesar_cipher_view_post_valid_encrypt_status_code(rf, caesar_cipher_url):
    """Test the status code for a valid POST request for encryption."""
    request = rf.post(
        caesar_cipher_url, data={'text': 'HELLO', 'shift': '3', 'mode': 'encrypt'}
    )
    response = caesar_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_caesar_cipher_view_post_valid_encrypt_response_data(rf, caesar_cipher_url):
    """Test the response data for a valid POST request for encryption."""
    request = rf.post(
        caesar_cipher_url, data={'text': 'HELLO', 'shift': '3', 'mode': 'encrypt'}
    )
    response = caesar_cipher_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {"result": "KHOOR"}

def test_caesar_cipher_view_post_invalid_shift_status_code(rf, caesar_cipher_url):
    """Test the status code for an invalid shift (non-integer)."""
    request = rf.post(
        caesar_cipher_url, data={'text': 'HELLO', 'shift': 'invalid', 'mode': 'encrypt'}
    )
    response = caesar_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_caesar_cipher_view_post_invalid_shift_response_data(rf, caesar_cipher_url):
    """Test the response data for an invalid shift (non-integer)."""
    request = rf.post(
        caesar_cipher_url, data={'text': 'HELLO', 'shift': 'invalid', 'mode': 'encrypt'}
    )
    response = caesar_cipher_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {'error': "Wrong shift type! invalid literal for int() with base 10: 'invalid'"}

def test_caesar_cipher_view_post_default_shift_and_mode_status_code(rf, caesar_cipher_url):
    """Test the status code for a POST request with default shift and mode."""
    request = rf.post(caesar_cipher_url, data={'text': 'HELLO'})
    response = caesar_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_caesar_cipher_view_post_default_shift_and_mode_response_data(rf, caesar_cipher_url):
    """Test the response data for a POST request with default shift and mode."""
    request = rf.post(caesar_cipher_url, data={'text': 'HELLO'})
    response = caesar_cipher_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {"result": "KHOOR"}  # Default shift is 3 and mode is 'encrypt'

def test_caesar_cipher_view_post_text_size_exceeds_limit_status_code(rf, caesar_cipher_url):
    """Test the status code for a POST request with text size exceeding the limit."""
    with pytest.raises(RequestDataTooBig):
        large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
        request = rf.post(caesar_cipher_url, data={'text': large_text, 'shift': '3', 'mode': 'encrypt'})
        caesar_cipher_view(request)
