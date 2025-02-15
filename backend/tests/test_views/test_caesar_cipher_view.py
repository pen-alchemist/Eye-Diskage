import pytest

from django.test import RequestFactory
from django.middleware.csrf import get_token

from rest_framework.response import Response
from rest_framework import status

from backend.views import caesar_cipher_view


@pytest.fixture
def request_factory():
    return RequestFactory()

def test_caesar_cipher_view_post_valid_encrypt_status_code(request_factory):
    """Test the status code for a valid POST request for encryption."""
    request = request_factory.post('/caesar-cipher/', data={'text': 'HELLO', 'shift': '3', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = caesar_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_caesar_cipher_view_post_valid_encrypt_response_type(request_factory):
    """Test the response type for a valid POST request for encryption."""
    request = request_factory.post('/caesar-cipher/', data={'text': 'HELLO', 'shift': '3', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = caesar_cipher_view(request)
    assert isinstance(response, Response)

def test_caesar_cipher_view_post_valid_encrypt_response_data(request_factory):
    """Test the response data for a valid POST request for encryption."""
    request = request_factory.post('/caesar-cipher/', data={'text': 'HELLO', 'shift': '3', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = caesar_cipher_view(request)
    assert response.data == {"result": "KHOOR"}

def test_caesar_cipher_view_post_invalid_shift_status_code(request_factory):
    """Test the status code for an invalid shift (non-integer)."""
    request = request_factory.post('/caesar-cipher/', data={'text': 'HELLO', 'shift': 'invalid', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = caesar_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_caesar_cipher_view_post_invalid_shift_response_type(request_factory):
    """Test the response type for an invalid shift (non-integer)."""
    request = request_factory.post('/caesar-cipher/', data={'text': 'HELLO', 'shift': 'invalid', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = caesar_cipher_view(request)
    assert isinstance(response, Response)

def test_caesar_cipher_view_post_invalid_shift_response_data(request_factory):
    """Test the response data for an invalid shift (non-integer)."""
    request = request_factory.post('/caesar-cipher/', data={'text': 'HELLO', 'shift': 'invalid', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = caesar_cipher_view(request)
    assert response.data == {"error": "Shift must be an integer."}

def test_caesar_cipher_view_post_default_shift_and_mode_status_code(request_factory):
    """Test the status code for a POST request with default shift and mode."""
    request = request_factory.post('/caesar-cipher/', data={'text': 'HELLO'})
    request.csrf_token = get_token(request)
    response = caesar_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_caesar_cipher_view_post_default_shift_and_mode_response_type(request_factory):
    """Test the response type for a POST request with default shift and mode."""
    request = request_factory.post('/caesar-cipher/', data={'text': 'HELLO'})
    request.csrf_token = get_token(request)
    response = caesar_cipher_view(request)
    assert isinstance(response, Response)

def test_caesar_cipher_view_post_default_shift_and_mode_response_data(request_factory):
    """Test the response data for a POST request with default shift and mode."""
    request = request_factory.post('/caesar-cipher/', data={'text': 'HELLO'})
    request.csrf_token = get_token(request)
    response = caesar_cipher_view(request)
    assert response.data == {"result": "KHOOR"}  # Default shift is 3 and mode is 'encrypt'

def test_caesar_cipher_view_post_text_size_exceeds_limit_status_code(request_factory):
    """Test the status code for a POST request with text size exceeding the limit."""
    large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
    request = request_factory.post('/caesar-cipher/', data={'text': large_text, 'shift': '3', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = caesar_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_caesar_cipher_view_post_text_size_exceeds_limit_response_type(request_factory):
    """Test the response type for a POST request with text size exceeding the limit."""
    large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
    request = request_factory.post('/caesar-cipher/', data={'text': large_text, 'shift': '3', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = caesar_cipher_view(request)
    assert isinstance(response, Response)

def test_caesar_cipher_view_post_text_size_exceeds_limit_response_data(request_factory):
    """Test the response data for a POST request with text size exceeding the limit."""
    large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
    request = request_factory.post('/caesar-cipher/', data={'text': large_text, 'shift': '3', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = caesar_cipher_view(request)
    assert response.data == {"error": "Text size exceeds the allowed limit."}
