import pytest

from django.test import RequestFactory
from django.urls import reverse

from rest_framework import status

from backend.views import caesar_cipher_view


@pytest.fixture
def rf():
    return RequestFactory()

def test_caesar_cipher_view_post_valid_encrypt_status_code(rf):
    """Test the status code for a valid POST request for encryption."""
    url = reverse('eye-caesar-text')
    request = rf.post(url, data={'text': 'HELLO', 'shift': '3', 'mode': 'encrypt'})
    response = caesar_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_caesar_cipher_view_post_valid_encrypt_response_data(rf):
    """Test the response data for a valid POST request for encryption."""
    url = reverse('eye-caesar-text')
    request = rf.post(url, data={'text': 'HELLO', 'shift': '3', 'mode': 'encrypt'})
    response = caesar_cipher_view(request)
    assert response.json() == {"result": "KHOOR"}

def test_caesar_cipher_view_post_invalid_shift_status_code(rf):
    """Test the status code for an invalid shift (non-integer)."""
    url = reverse('eye-caesar-text')
    request = rf.post(url, data={'text': 'HELLO', 'shift': 'invalid', 'mode': 'encrypt'})
    response = caesar_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_caesar_cipher_view_post_invalid_shift_response_data(rf):
    """Test the response data for an invalid shift (non-integer)."""
    url = reverse('eye-caesar-text')
    request = rf.post(url, data={'text': 'HELLO', 'shift': 'invalid', 'mode': 'encrypt'})
    response = caesar_cipher_view(request)
    assert response.json() == {"error": "Shift must be an integer."}

def test_caesar_cipher_view_post_default_shift_and_mode_status_code(rf):
    """Test the status code for a POST request with default shift and mode."""
    url = reverse('eye-caesar-text')
    request = rf.post(url, data={'text': 'HELLO'})
    response = caesar_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_caesar_cipher_view_post_default_shift_and_mode_response_data(rf):
    """Test the response data for a POST request with default shift and mode."""
    url = reverse('eye-caesar-text')
    request = rf.post(url, data={'text': 'HELLO'})
    response = caesar_cipher_view(request)
    assert response.json() == {"result": "KHOOR"}  # Default shift is 3 and mode is 'encrypt'

def test_caesar_cipher_view_post_text_size_exceeds_limit_status_code(rf):
    """Test the status code for a POST request with text size exceeding the limit."""
    url = reverse('eye-caesar-text')
    large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
    request = rf.post(url, data={'text': large_text, 'shift': '3', 'mode': 'encrypt'})
    response = caesar_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_caesar_cipher_view_post_text_size_exceeds_limit_response_data(rf):
    """Test the response data for a POST request with text size exceeding the limit."""
    url = reverse('eye-caesar-text')
    large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
    request = rf.post(url, data={'text': large_text, 'shift': '3', 'mode': 'encrypt'})
    response = caesar_cipher_view(request)
    assert response.json() == {"error": "Text size exceeds the allowed limit."}
