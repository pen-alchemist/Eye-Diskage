import json
import pytest

from django.core.exceptions import RequestDataTooBig
from django.test import RequestFactory

from rest_framework import status
from backend.views import vigenere_cipher_view


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.fixture
def vigenere_cipher_url():
    return "/api/eye_diskage/vigenere-cipher/"


@pytest.fixture
def valid_encrypt_data():
    return {'text': 'HELLO', 'key': 'KEY', 'mode': 'encrypt'}


@pytest.fixture
def valid_decrypt_data():
    return {'text': 'RIJVS', 'key': 'KEY', 'mode': 'decrypt'}


def test_vigenere_cipher_view_post_valid_encrypt_status_code(rf, vigenere_cipher_url, valid_encrypt_data):
    """Test the status code for a valid POST request for encryption."""
    request = rf.post(vigenere_cipher_url, data=valid_encrypt_data)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK


def test_vigenere_cipher_view_post_valid_encrypt_response_type(rf, vigenere_cipher_url, valid_encrypt_data):
    """Test the response type for a valid POST request for encryption."""
    request = rf.post(vigenere_cipher_url, data=valid_encrypt_data)
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'text/html; charset=utf-8'


def test_vigenere_cipher_view_post_valid_encrypt_response_data(rf, vigenere_cipher_url, valid_encrypt_data):
    """Test the response data for a valid POST request for encryption."""
    request = rf.post(vigenere_cipher_url, data=valid_encrypt_data)
    response = vigenere_cipher_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {"result": "RIJVS"}


def test_vigenere_cipher_view_post_valid_decrypt_status_code(rf, vigenere_cipher_url, valid_decrypt_data):
    """Test the status code for a valid POST request for decryption."""
    request = rf.post(vigenere_cipher_url, data=valid_decrypt_data)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK


def test_vigenere_cipher_view_post_valid_decrypt_response_type(rf, vigenere_cipher_url, valid_decrypt_data):
    """Test the response type for a valid POST request for decryption."""
    request = rf.post(vigenere_cipher_url, data=valid_decrypt_data)
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'text/html; charset=utf-8'


def test_vigenere_cipher_view_post_valid_decrypt_response_data(rf, vigenere_cipher_url, valid_decrypt_data):
    """Test the response data for a valid POST request for decryption."""
    request = rf.post(vigenere_cipher_url, data=valid_decrypt_data)
    response = vigenere_cipher_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {"result": "HELLO"}


def test_vigenere_cipher_view_post_missing_key_status_code(rf, vigenere_cipher_url):
    """Test the status code for a POST request with a missing key."""
    request = rf.post(vigenere_cipher_url, data={'text': 'HELLO', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_vigenere_cipher_view_post_missing_key_response_type(rf, vigenere_cipher_url):
    """Test the response type for a POST request with a missing key."""
    request = rf.post(vigenere_cipher_url, data={'text': 'HELLO', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'text/html; charset=utf-8'


def test_vigenere_cipher_view_post_missing_key_response_data(rf, vigenere_cipher_url):
    """Test the response data for a POST request with a missing key."""
    request = rf.post(vigenere_cipher_url, data={'text': 'HELLO', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {"error": "Key is required."}


def test_vigenere_cipher_view_post_empty_key_status_code(rf, vigenere_cipher_url):
    """Test the status code for a POST request with an empty key."""
    request = rf.post(vigenere_cipher_url, data={'text': 'HELLO', 'key': '', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_vigenere_cipher_view_post_empty_key_response_type(rf, vigenere_cipher_url):
    """Test the response type for a POST request with an empty key."""
    request = rf.post(vigenere_cipher_url, data={'text': 'HELLO', 'key': '', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'text/html; charset=utf-8'


def test_vigenere_cipher_view_post_empty_key_response_data(rf, vigenere_cipher_url):
    """Test the response data for a POST request with an empty key."""
    request = rf.post(vigenere_cipher_url, data={'text': 'HELLO', 'key': '', 'mode': 'encrypt'})
    response = vigenere_cipher_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {"error": "Key is required."}


def test_vigenere_cipher_view_post_text_size_exceeds_limit_response_data(rf, vigenere_cipher_url):
    """Test the response data for a POST request with text size exceeding the limit."""
    with pytest.raises(RequestDataTooBig):
        large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
        request = rf.post(vigenere_cipher_url, data={'text': large_text, 'key': 'KEY', 'mode': 'encrypt'})
        vigenere_cipher_view(request)


def test_vigenere_cipher_view_post_invalid_mode_status_code(rf, vigenere_cipher_url):
    """Test the status code for a POST request with an invalid mode."""
    request = rf.post(vigenere_cipher_url, data={'text': 'HELLO', 'key': 'KEY', 'mode': 'invalid_mode'})
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK


def test_vigenere_cipher_view_post_invalid_mode_response_type(rf, vigenere_cipher_url):
    """Test the response type for a POST request with an invalid mode."""
    request = rf.post(vigenere_cipher_url, data={'text': 'HELLO', 'key': 'KEY', 'mode': 'invalid_mode'})
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'text/html; charset=utf-8'


def test_vigenere_cipher_view_post_invalid_mode_response_data(rf, vigenere_cipher_url):
    """Test the response data for a POST request with an invalid mode."""
    request = rf.post(vigenere_cipher_url, data={'text': 'HELLO', 'key': 'KEY', 'mode': 'invalid_mode'})
    response = vigenere_cipher_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert "result" in json_data


def test_vigenere_cipher_view_get_request_status_code(rf, vigenere_cipher_url):
    """Test the status code for an invalid GET request."""
    request = rf.get(vigenere_cipher_url)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


def test_vigenere_cipher_view_get_request_response_type(rf, vigenere_cipher_url):
    """Test the response type for an invalid GET request."""
    request = rf.get(vigenere_cipher_url)
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'text/html; charset=utf-8'


def test_vigenere_cipher_view_get_request_response_data(rf, vigenere_cipher_url):
    """Test the response data for an invalid GET request."""
    request = rf.get(vigenere_cipher_url)
    response = vigenere_cipher_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {'detail': 'Method "GET" not allowed.'}


def test_vigenere_cipher_view_put_request_status_code(rf, vigenere_cipher_url):
    """Test the status code for an invalid PUT request."""
    request = rf.put(vigenere_cipher_url)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


def test_vigenere_cipher_view_put_request_response_type(rf, vigenere_cipher_url):
    """Test the response type for an invalid PUT request."""
    request = rf.put(vigenere_cipher_url)
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'text/html; charset=utf-8'


def test_vigenere_cipher_view_put_request_response_data(rf, vigenere_cipher_url):
    """Test the response data for an invalid PUT request."""
    request = rf.put(vigenere_cipher_url)
    response = vigenere_cipher_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {'detail': 'Method "PUT" not allowed.'}


def test_vigenere_cipher_view_delete_request_status_code(rf, vigenere_cipher_url):
    """Test the status code for an invalid DELETE request."""
    request = rf.delete(vigenere_cipher_url)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


def test_vigenere_cipher_view_delete_request_response_type(rf, vigenere_cipher_url):
    """Test the response type for an invalid DELETE request."""
    request = rf.delete(vigenere_cipher_url)
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'text/html; charset=utf-8'


def test_vigenere_cipher_view_delete_request_response_data(rf, vigenere_cipher_url):
    """Test the response data for an invalid DELETE request."""
    request = rf.delete(vigenere_cipher_url)
    response = vigenere_cipher_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {'detail': 'Method "DELETE" not allowed.'}


def test_vigenere_cipher_view_patch_request_status_code(rf, vigenere_cipher_url):
    """Test the status code for an invalid PATCH request."""
    request = rf.patch(vigenere_cipher_url)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


def test_vigenere_cipher_view_patch_request_response_type(rf, vigenere_cipher_url):
    """Test the response type for an invalid PATCH request."""
    request = rf.patch(vigenere_cipher_url)
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'text/html; charset=utf-8'


def test_vigenere_cipher_view_patch_request_response_data(rf, vigenere_cipher_url):
    """Test the response data for an invalid PATCH request."""
    request = rf.patch(vigenere_cipher_url)
    response = vigenere_cipher_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {'detail': 'Method "PATCH" not allowed.'}


def test_vigenere_cipher_view_with_allowany_permission_status_code(rf, vigenere_cipher_url, valid_encrypt_data):
    """Test the status code for a POST request with AllowAny permission."""
    request = rf.post(vigenere_cipher_url, data=valid_encrypt_data)
    response = vigenere_cipher_view(request)
    assert response.status_code == status.HTTP_200_OK


def test_vigenere_cipher_view_with_allowany_permission_response_type(rf, vigenere_cipher_url, valid_encrypt_data):
    """Test the response type for a POST request with AllowAny permission."""
    request = rf.post(vigenere_cipher_url, data=valid_encrypt_data)
    response = vigenere_cipher_view(request)
    assert response['Content-Type'] == 'text/html; charset=utf-8'


def test_vigenere_cipher_view_with_allowany_permission_response_data(rf, vigenere_cipher_url, valid_encrypt_data):
    """Test the response data for a POST request with AllowAny permission."""
    request = rf.post(vigenere_cipher_url, data=valid_encrypt_data)
    response = vigenere_cipher_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {"result": "RIJVS"}
