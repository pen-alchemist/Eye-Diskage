import pytest

from django.test import RequestFactory
from django.urls import reverse

from rest_framework import status

from backend.views import vigenere_cipher_view


@pytest.fixture
def rf():
    return RequestFactory()

def test_vigenere_cipher_view_post_valid_encrypt_status_code(rf):
    """Test the status code for a valid POST request for encryption."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'HELLO', 'key': 'KEY', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_vigenere_cipher_view_post_valid_encrypt_response_type(rf):
    """Test the response type for a valid POST request for encryption."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'HELLO', 'key': 'KEY', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'application/json'

def test_vigenere_cipher_view_post_valid_encrypt_response_data(rf):
    """Test the response data for a valid POST request for encryption."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'HELLO', 'key': 'KEY', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    response_data = response.json()
    assert response_data == {"result": "RIJVS"}

def test_vigenere_cipher_view_post_valid_decrypt_status_code(rf):
    """Test the status code for a valid POST request for decryption."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'RIJVS', 'key': 'KEY', 'mode': 'decrypt'})
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_vigenere_cipher_view_post_valid_decrypt_response_type(rf):
    """Test the response type for a valid POST request for decryption."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'RIJVS', 'key': 'KEY', 'mode': 'decrypt'})
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'application/json'

def test_vigenere_cipher_view_post_valid_decrypt_response_data(rf):
    """Test the response data for a valid POST request for decryption."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'RIJVS', 'key': 'KEY', 'mode': 'decrypt'})
    response = vigenere_cipher_view(request)
    response_data = response.json()
    assert response_data == {"result": "HELLO"}

def test_vigenere_cipher_view_post_missing_key_status_code(rf):
    """Test the status code for a POST request with a missing key."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'HELLO', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_post_missing_key_response_type(rf):
    """Test the response type for a POST request with a missing key."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'HELLO', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'application/json'

def test_vigenere_cipher_view_post_missing_key_response_data(rf):
    """Test the response data for a POST request with a missing key."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'HELLO', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    response_data = response.json()
    assert response_data == {"error": "Key is required."}

def test_vigenere_cipher_view_post_empty_key_status_code(rf):
    """Test the status code for a POST request with an empty key."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'HELLO', 'key': '', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_post_empty_key_response_type(rf):
    """Test the response type for a POST request with an empty key."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'HELLO', 'key': '', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'application/json'

def test_vigenere_cipher_view_post_empty_key_response_data(rf):
    """Test the response data for a POST request with an empty key."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'HELLO', 'key': '', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    response_data = response.json()
    assert response_data == {"error": "Key is required."}

def test_vigenere_cipher_view_post_text_size_exceeds_limit_status_code(rf):
    """Test the status code for a POST request with text size exceeding the limit."""
    url = reverse('eye-vigenere-text')
    large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
    request = rf.post(url, data={'text': large_text, 'key': 'KEY', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_post_text_size_exceeds_limit_response_type(rf):
    """Test the response type for a POST request with text size exceeding the limit."""
    url = reverse('eye-vigenere-text')
    large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
    request = rf.post(url, data={'text': large_text, 'key': 'KEY', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'application/json'

def test_vigenere_cipher_view_post_text_size_exceeds_limit_response_data(rf):
    """Test the response data for a POST request with text size exceeding the limit."""
    url = reverse('eye-vigenere-text')
    large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
    request = rf.post(url, data={'text': large_text, 'key': 'KEY', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    response_data = response.json()
    assert response_data == {"error": "Text size exceeds the allowed limit."}

def test_vigenere_cipher_view_post_invalid_mode_status_code(rf):
    """Test the status code for a POST request with an invalid mode."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'HELLO', 'key': 'KEY', 'mode': 'invalid_mode'})
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_post_invalid_mode_response_type(rf):
    """Test the response type for a POST request with an invalid mode."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'HELLO', 'key': 'KEY', 'mode': 'invalid_mode'})
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'application/json'

def test_vigenere_cipher_view_post_invalid_mode_response_data(rf):
    """Test the response data for a POST request with an invalid mode."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'HELLO', 'key': 'KEY', 'mode': 'invalid_mode'})
    response = vigenere_cipher_view(request)
    response_data = response.json()
    assert "error" in response_data

def test_vigenere_cipher_view_get_request_status_code(rf):
    """Test the status code for an invalid GET request."""
    url = reverse('eye-vigenere-text')
    request = rf.get(url)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_get_request_response_type(rf):
    """Test the response type for an invalid GET request."""
    url = reverse('eye-vigenere-text')
    request = rf.get(url)
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'application/json'

def test_vigenere_cipher_view_get_request_response_data(rf):
    """Test the response data for an invalid GET request."""
    url = reverse('eye-vigenere-text')
    request = rf.get(url)
    response = vigenere_cipher_view(request)
    response_data = response.json()
    assert response_data == {"error": "Invalid request method."}

def test_vigenere_cipher_view_put_request_status_code(rf):
    """Test the status code for an invalid PUT request."""
    url = reverse('eye-vigenere-text')
    request = rf.put(url)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_put_request_response_type(rf):
    """Test the response type for an invalid PUT request."""
    url = reverse('eye-vigenere-text')
    request = rf.put(url)
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'application/json'

def test_vigenere_cipher_view_put_request_response_data(rf):
    """Test the response data for an invalid PUT request."""
    url = reverse('eye-vigenere-text')
    request = rf.put(url)
    response = vigenere_cipher_view(request)
    response_data = response.json()
    assert response_data == {"error": "Invalid request method."}

def test_vigenere_cipher_view_delete_request_status_code(rf):
    """Test the status code for an invalid DELETE request."""
    url = reverse('eye-vigenere-text')
    request = rf.delete(url)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_delete_request_response_type(rf):
    """Test the response type for an invalid DELETE request."""
    url = reverse('eye-vigenere-text')
    request = rf.delete(url)
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'application/json'

def test_vigenere_cipher_view_delete_request_response_data(rf):
    """Test the response data for an invalid DELETE request."""
    url = reverse('eye-vigenere-text')
    request = rf.delete(url)
    response = vigenere_cipher_view(request)
    response_data = response.json()
    assert response_data == {"error": "Invalid request method."}

def test_vigenere_cipher_view_patch_request_status_code(rf):
    """Test the status code for an invalid PATCH request."""
    url = reverse('eye-vigenere-text')
    request = rf.patch(url)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_vigenere_cipher_view_patch_request_response_type(rf):
    """Test the response type for an invalid PATCH request."""
    url = reverse('geneeye-django-genrator')
    request = rf.patch(url)
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'application/json'

def test_vigenere_cipher_view_patch_request_response_data(rf):
    """Test the response data for an invalid PATCH request."""
    url = reverse('eye-vigenere-text')
    request = rf.patch(url)
    response = vigenere_cipher_view(request)
    response_data = response.json()
    assert response_data == {"error": "Invalid request method."}

def test_vigenere_cipher_view_with_allowany_permission_status_code(rf):
    """Test the status code for a POST request with AllowAny permission."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'HELLO', 'key': 'KEY', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_vigenere_cipher_view_with_allowany_permission_response_type(rf):
    """Test the response type for a POST request with AllowAny permission."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'HELLO', 'key': 'KEY', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'application/json'

def test_vigenere_cipher_view_with_allowany_permission_response_data(rf):
    """Test the response data for a POST request with AllowAny permission."""
    url = reverse('eye-vigenere-text')
    request = rf.post(url, data={'text': 'HELLO', 'key': 'KEY', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    response_data = response.json()
    assert response_data == {"result": "RIJVS"}
