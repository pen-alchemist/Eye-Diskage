import pytest

from django.test import RequestFactory
from django.middleware.csrf import get_token

from rest_framework.response import Response
from rest_framework import status

from backend.views import vigenere_cipher_view


@pytest.fixture
def request_factory():
    return RequestFactory()

def test_vigenere_cipher_view_post_valid_encrypt_status_code(request_factory):
    """Test the status code for a valid POST request for encryption."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'HELLO', 'key': 'KEY', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_vigenere_cipher_view_post_valid_encrypt_response_type(request_factory):
    """Test the response type for a valid POST request for encryption."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'HELLO', 'key': 'KEY', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert isinstance(response, Response)

def test_vigenere_cipher_view_post_valid_encrypt_response_data(request_factory):
    """Test the response data for a valid POST request for encryption."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'HELLO', 'key': 'KEY', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert response.data == {"result": "RIJVS"}

def test_vigenere_cipher_view_post_valid_decrypt_status_code(request_factory):
    """Test the status code for a valid POST request for decryption."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'RIJVS', 'key': 'KEY', 'mode': 'decrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_vigenere_cipher_view_post_valid_decrypt_response_type(request_factory):
    """Test the response type for a valid POST request for decryption."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'RIJVS', 'key': 'KEY', 'mode': 'decrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert isinstance(response, Response)

def test_vigenere_cipher_view_post_valid_decrypt_response_data(request_factory):
    """Test the response data for a valid POST request for decryption."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'RIJVS', 'key': 'KEY', 'mode': 'decrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert response.data == {"result": "HELLO"}

def test_vigenere_cipher_view_post_missing_key_status_code(request_factory):
    """Test the status code for a POST request with a missing key."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'HELLO', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_post_missing_key_response_type(request_factory):
    """Test the response type for a POST request with a missing key."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'HELLO', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert isinstance(response, Response)

def test_vigenere_cipher_view_post_missing_key_response_data(request_factory):
    """Test the response data for a POST request with a missing key."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'HELLO', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert response.data == {"error": "Key is required."}

def test_vigenere_cipher_view_post_empty_key_status_code(request_factory):
    """Test the status code for a POST request with an empty key."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'HELLO', 'key': '', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_post_empty_key_response_type(request_factory):
    """Test the response type for a POST request with an empty key."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'HELLO', 'key': '', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert isinstance(response, Response)

def test_vigenere_cipher_view_post_empty_key_response_data(request_factory):
    """Test the response data for a POST request with an empty key."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'HELLO', 'key': '', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert response.data == {"error": "Key is required."}

def test_vigenere_cipher_view_post_text_size_exceeds_limit_status_code(request_factory):
    """Test the status code for a POST request with text size exceeding the limit."""
    large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
    request = request_factory.post('/vigenere-cipher/', data={'text': large_text, 'key': 'KEY', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_post_text_size_exceeds_limit_response_type(request_factory):
    """Test the response type for a POST request with text size exceeding the limit."""
    large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
    request = request_factory.post('/vigenere-cipher/', data={'text': large_text, 'key': 'KEY', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert isinstance(response, Response)

def test_vigenere_cipher_view_post_text_size_exceeds_limit_response_data(request_factory):
    """Test the response data for a POST request with text size exceeding the limit."""
    large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
    request = request_factory.post('/vigenere-cipher/', data={'text': large_text, 'key': 'KEY', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert response.data == {"error": "Text size exceeds the allowed limit."}

def test_vigenere_cipher_view_post_invalid_mode_status_code(request_factory):
    """Test the status code for a POST request with an invalid mode."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'HELLO', 'key': 'KEY', 'mode': 'invalid_mode'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_post_invalid_mode_response_type(request_factory):
    """Test the response type for a POST request with an invalid mode."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'HELLO', 'key': 'KEY', 'mode': 'invalid_mode'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert isinstance(response, Response)

def test_vigenere_cipher_view_post_invalid_mode_response_data(request_factory):
    """Test the response data for a POST request with an invalid mode."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'HELLO', 'key': 'KEY', 'mode': 'invalid_mode'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert "error" in response.data

def test_vigenere_cipher_view_get_request_status_code(request_factory):
    """Test the status code for an invalid GET request."""
    request = request_factory.get('/vigenere-cipher/')
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_get_request_response_type(request_factory):
    """Test the response type for an invalid GET request."""
    request = request_factory.get('/vigenere-cipher/')
    response = vigenere_cipher_view(request)
    assert isinstance(response, Response)

def test_vigenere_cipher_view_get_request_response_data(request_factory):
    """Test the response data for an invalid GET request."""
    request = request_factory.get('/vigenere-cipher/')
    response = vigenere_cipher_view(request)
    assert response.data == {"error": "Invalid request method."}

def test_vigenere_cipher_view_put_request_status_code(request_factory):
    """Test the status code for an invalid PUT request."""
    request = request_factory.put('/vigenere-cipher/')
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_put_request_response_type(request_factory):
    """Test the response type for an invalid PUT request."""
    request = request_factory.put('/vigenere-cipher/')
    response = vigenere_cipher_view(request)
    assert isinstance(response, Response)

def test_vigenere_cipher_view_put_request_response_data(request_factory):
    """Test the response data for an invalid PUT request."""
    request = request_factory.put('/vigenere-cipher/')
    response = vigenere_cipher_view(request)
    assert response.data == {"error": "Invalid request method."}

def test_vigenere_cipher_view_delete_request_status_code(request_factory):
    """Test the status code for an invalid DELETE request."""
    request = request_factory.delete('/vigenere-cipher/')
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_delete_request_response_type(request_factory):
    """Test the response type for an invalid DELETE request."""
    request = request_factory.delete('/vigenere-cipher/')
    response = vigenere_cipher_view(request)
    assert isinstance(response, Response)

def test_vigenere_cipher_view_delete_request_response_data(request_factory):
    """Test the response data for an invalid DELETE request."""
    request = request_factory.delete('/vigenere-cipher/')
    response = vigenere_cipher_view(request)
    assert response.data == {"error": "Invalid request method."}

def test_vigenere_cipher_view_patch_request_status_code(request_factory):
    """Test the status code for an invalid PATCH request."""
    request = request_factory.patch('/vigenere-cipher/')
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_patch_request_response_type(request_factory):
    """Test the response type for an invalid PATCH request."""
    request = request_factory.patch('/vigenere-cipher/')
    response = vigenere_cipher_view(request)
    assert isinstance(response, Response)

def test_vigenere_cipher_view_patch_request_response_data(request_factory):
    """Test the response data for an invalid PATCH request."""
    request = request_factory.patch('/vigenere-cipher/')
    response = vigenere_cipher_view(request)
    assert response.data == {"error": "Invalid request method."}

def test_vigenere_cipher_view_with_allowany_permission_status_code(request_factory):
    """Test the status code for a POST request with AllowAny permission."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'HELLO', 'key': 'KEY', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_vigenere_cipher_view_with_allowany_permission_response_type(request_factory):
    """Test the response type for a POST request with AllowAny permission."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'HELLO', 'key': 'KEY', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert isinstance(response, Response)

def test_vigenere_cipher_view_with_allowany_permission_response_data(request_factory):
    """Test the response data for a POST request with AllowAny permission."""
    request = request_factory.post('/vigenere-cipher/', data={'text': 'HELLO', 'key': 'KEY', 'mode': 'encrypt'})
    request.csrf_token = get_token(request)
    response = vigenere_cipher_view(request)
    assert response.data == {"result": "RIJVS"}
