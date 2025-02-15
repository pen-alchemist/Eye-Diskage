import json
import pytest

from django.test import RequestFactory
from django.middleware.csrf import get_token
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework import status

from backend.views import generator_view


@pytest.fixture
def request_factory():
    return RequestFactory()

def test_generator_view_post_valid_request_status_code(request_factory):
    """Test the status code for a valid POST request."""
    request = request_factory.post('/generator/')
    request.csrf_token = get_token(request)  # Simulate CSRF token
    response = generator_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_generator_view_post_valid_request_response_type(request_factory):
    """Test the response type for a valid POST request."""
    request = request_factory.post('/generator/')
    request.csrf_token = get_token(request)  # Simulate CSRF token
    response = generator_view(request)
    assert isinstance(response, JsonResponse)

def test_generator_view_post_valid_request_response_data_has_key(request_factory):
    """Test that the response data contains a 'key' field for a valid POST request."""
    request = request_factory.post('/generator/')
    request.csrf_token = get_token(request)  # Simulate CSRF token
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert 'key' in response_data

def test_generator_view_post_valid_request_response_data_key_not_empty(request_factory):
    """Test that the 'key' in the response data is not empty for a valid POST request."""
    request = request_factory.post('/generator/')
    request.csrf_token = get_token(request)  # Simulate CSRF token
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert len(response_data['key']) > 0

def test_generator_view_post_invalid_csrf_status_code(request_factory):
    """Test the status code for a POST request without a CSRF token."""
    request = request_factory.post('/generator/')
    # No CSRF token is added to the request
    response = generator_view(request)
    assert response.status_code == status.HTTP_403_FORBIDDEN  # CSRF failure

def test_generator_view_get_request_status_code(request_factory):
    """Test the status code for an invalid GET request."""
    request = request_factory.get('/generator/')
    response = generator_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_generator_view_get_request_response_type(request_factory):
    """Test the response type for an invalid GET request."""
    request = request_factory.get('/generator/')
    response = generator_view(request)
    assert isinstance(response, Response)

def test_generator_view_get_request_response_data(request_factory):
    """Test the response data for an invalid GET request."""
    request = request_factory.get('/generator/')
    response = generator_view(request)
    assert response.data == {"error": "Invalid request method."}

def test_generator_view_put_request_status_code(request_factory):
    """Test the status code for an invalid PUT request."""
    request = request_factory.put('/generator/')
    response = generator_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_generator_view_put_request_response_type(request_factory):
    """Test the response type for an invalid PUT request."""
    request = request_factory.put('/generator/')
    response = generator_view(request)
    assert isinstance(response, Response)

def test_generator_view_put_request_response_data(request_factory):
    """Test the response data for an invalid PUT request."""
    request = request_factory.put('/generator/')
    response = generator_view(request)
    assert response.data == {"error": "Invalid request method."}

def test_generator_view_delete_request_status_code(request_factory):
    """Test the status code for an invalid DELETE request."""
    request = request_factory.delete('/generator/')
    response = generator_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_generator_view_delete_request_response_type(request_factory):
    """Test the response type for an invalid DELETE request."""
    request = request_factory.delete('/generator/')
    response = generator_view(request)
    assert isinstance(response, Response)

def test_generator_view_delete_request_response_data(request_factory):
    """Test the response data for an invalid DELETE request."""
    request = request_factory.delete('/generator/')
    response = generator_view(request)
    assert response.data == {"error": "Invalid request method."}

def test_generator_view_patch_request_status_code(request_factory):
    """Test the status code for an invalid PATCH request."""
    request = request_factory.patch('/generator/')
    response = generator_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_generator_view_patch_request_response_type(request_factory):
    """Test the response type for an invalid PATCH request."""
    request = request_factory.patch('/generator/')
    response = generator_view(request)
    assert isinstance(response, Response)

def test_generator_view_patch_request_response_data(request_factory):
    """Test the response data for an invalid PATCH request."""
    request = request_factory.patch('/generator/')
    response = generator_view(request)
    assert response.data == {"error": "Invalid request method."}

def test_generator_view_with_allowany_permission_status_code(request_factory):
    """Test the status code for a POST request with AllowAny permission."""
    request = request_factory.post('/generator/')
    request.csrf_token = get_token(request)  # Simulate CSRF token
    response = generator_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_generator_view_with_allowany_permission_response_type(request_factory):
    """Test the response type for a POST request with AllowAny permission."""
    request = request_factory.post('/generator/')
    request.csrf_token = get_token(request)  # Simulate CSRF token
    response = generator_view(request)
    assert isinstance(response, JsonResponse)

def test_generator_view_with_allowany_permission_response_data_has_key(request_factory):
    """Test that the response data contains a 'key' field for a POST request with AllowAny permission."""
    request = request_factory.post('/generator/')
    request.csrf_token = get_token(request)  # Simulate CSRF token
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert 'key' in response_data

def test_generator_view_with_allowany_permission_response_data_key_not_empty(request_factory):
    """Test that the 'key' in the response data is not empty for a POST request with AllowAny permission."""
    request = request_factory.post('/generator/')
    request.csrf_token = get_token(request)  # Simulate CSRF token
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert len(response_data['key']) > 0
