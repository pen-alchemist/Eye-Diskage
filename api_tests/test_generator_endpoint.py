import json

from rest_framework import status

from backend.views import generator_view


def test_generator_view_post_valid_request_status_code(rf, caesar_cipher_url):
    """Test the status code for a valid POST request."""
    request = rf.post(caesar_cipher_url)
    response = generator_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_generator_view_post_valid_request_response_type(rf, caesar_cipher_url):
    """Test the response type for a valid POST request."""
    request = rf.post(caesar_cipher_url)
    response = generator_view(request)
    assert response['Content-Type'] == 'application/json'

def test_generator_view_post_valid_request_response_data_has_key(rf, caesar_cipher_url):
    """Test that the response data contains a 'key' field for a valid POST request."""
    request = rf.post(caesar_cipher_url)
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert 'key' in response_data

def test_generator_view_post_valid_request_response_data_key_not_empty(rf, caesar_cipher_url):
    """Test that the 'key' in the response data is not empty for a valid POST request."""
    request = rf.post(caesar_cipher_url)
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert len(response_data['key']) > 0

def test_generator_view_get_request_status_code(rf, caesar_cipher_url):
    """Test the status code for an invalid GET request."""
    request = rf.get(caesar_cipher_url)
    response = generator_view(request)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_generator_view_get_request_response_type(rf, caesar_cipher_url):
    """Test the response type for an invalid GET request."""
    request = rf.get(caesar_cipher_url)
    response = generator_view(request)
    assert response['Content-Type'] == 'text/html; charset=utf-8'

def test_generator_view_get_request_response_data(rf, caesar_cipher_url):
    """Test the response data for an invalid GET request."""
    request = rf.get(caesar_cipher_url)
    response = generator_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {'detail': 'Method "GET" not allowed.'}

def test_generator_view_put_request_status_code(rf, caesar_cipher_url):
    """Test the status code for an invalid PUT request."""
    request = rf.put(caesar_cipher_url)
    response = generator_view(request)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_generator_view_put_request_response_type(rf, caesar_cipher_url):
    """Test the response type for an invalid PUT request."""
    request = rf.put(caesar_cipher_url)
    response = generator_view(request)
    assert response['Content-Type'] == 'text/html; charset=utf-8'

def test_generator_view_put_request_response_data(rf, caesar_cipher_url):
    """Test the response data for an invalid PUT request."""
    request = rf.put(caesar_cipher_url)
    response = generator_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {'detail': 'Method "PUT" not allowed.'}

def test_generator_view_delete_request_status_code(rf, caesar_cipher_url):
    """Test the status code for an invalid DELETE request."""
    request = rf.delete(caesar_cipher_url)
    response = generator_view(request)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_generator_view_delete_request_response_type(rf, caesar_cipher_url):
    """Test the response type for an invalid DELETE request."""
    request = rf.delete(caesar_cipher_url)
    response = generator_view(request)
    assert response['Content-Type'] == 'text/html; charset=utf-8'

def test_generator_view_delete_request_response_data(rf, caesar_cipher_url):
    """Test the response data for an invalid DELETE request."""
    request = rf.delete(caesar_cipher_url)
    response = generator_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {'detail': 'Method "DELETE" not allowed.'}

def test_generator_view_patch_request_status_code(rf, caesar_cipher_url):
    """Test the status code for an invalid PATCH request."""
    request = rf.patch(caesar_cipher_url)
    response = generator_view(request)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_generator_view_patch_request_response_type(rf, caesar_cipher_url):
    """Test the response type for an invalid PATCH request."""
    request = rf.patch(caesar_cipher_url)
    response = generator_view(request)
    assert response['Content-Type'] == 'text/html; charset=utf-8'

def test_generator_view_patch_request_response_data(rf, caesar_cipher_url):
    """Test the response data for an invalid PATCH request."""
    request = rf.patch(caesar_cipher_url)
    response = generator_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {'detail': 'Method "PATCH" not allowed.'}

def test_generator_view_with_allowany_permission_status_code(rf, caesar_cipher_url):
    """Test the status code for a POST request with AllowAny permission."""
    request = rf.post(caesar_cipher_url)
    response = generator_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_generator_view_with_allowany_permission_response_type(rf, caesar_cipher_url):
    """Test the response type for a POST request with AllowAny permission."""
    request = rf.post(caesar_cipher_url)
    response = generator_view(request)
    assert response['Content-Type'] == 'application/json'

def test_generator_view_with_allowany_permission_response_data_has_key(rf, caesar_cipher_url):
    """Test that the response data contains a 'key' field for a POST request with AllowAny permission."""
    request = rf.post(caesar_cipher_url)
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert 'key' in response_data

def test_generator_view_with_allowany_permission_response_data_key_not_empty(rf, caesar_cipher_url):
    """Test that the 'key' in the response data is not empty for a POST request with AllowAny permission."""
    request = rf.post(caesar_cipher_url)
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert len(response_data['key']) > 0
