import json
import pytest

from django.test import RequestFactory
from django.urls import reverse

from rest_framework import status

from backend.views import generator_view


@pytest.fixture
def rf():
    return RequestFactory()

def test_generator_view_post_valid_request_status_code(rf):
    """Test the status code for a valid POST request."""
    url = reverse('eye-django-gen')
    request = rf.post(url)
    response = generator_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_generator_view_post_valid_request_response_type(rf):
    """Test the response type for a valid POST request."""
    url = reverse('eye-django-gen')
    request = rf.post(url)
    response = generator_view(request)
    assert response['Content-Type'] == 'application/json'

def test_generator_view_post_valid_request_response_data_has_key(rf):
    """Test that the response data contains a 'key' field for a valid POST request."""
    url = reverse('eye-django-gen')
    request = rf.post(url)
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert 'key' in response_data

def test_generator_view_post_valid_request_response_data_key_not_empty(rf):
    """Test that the 'key' in the response data is not empty for a valid POST request."""
    url = reverse('eye-django-gen')
    request = rf.post(url)
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert len(response_data['key']) > 0

def test_generator_view_post_invalid_csrf_status_code(rf):
    """Test the status code for a POST request without a CSRF token."""
    url = reverse('eye-django-gen')
    request = rf.post(url)
    response = generator_view(request)
    assert response.status_code == status.HTTP_403_FORBIDDEN  # CSRF failure

def test_generator_view_get_request_status_code(rf):
    """Test the status code for an invalid GET request."""
    url = reverse('eye-django-gen')
    request = rf.get(url)
    response = generator_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_generator_view_get_request_response_type(rf):
    """Test the response type for an invalid GET request."""
    url = reverse('eye-django-gen')
    request = rf.get(url)
    response = generator_view(request)
    assert response['Content-Type'] == 'application/json'

def test_generator_view_get_request_response_data(rf):
    """Test the response data for an invalid GET request."""
    url = reverse('geneye-django-generator')
    request = rf.get(url)
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert response_data == {"error": "Invalid request method."}

def test_generator_view_put_request_status_code(rf):
    """Test the status code for an invalid PUT request."""
    url = reverse('eye-django-gen')
    request = rf.put(url)
    response = generator_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_generator_view_put_request_response_type(rf):
    """Test the response type for an invalid PUT request."""
    url = reverse('eye-django-gen')
    request = rf.put(url)
    response = generator_view(request)
    assert response['Content-Type'] == 'application/json'

def test_generator_view_put_request_response_data(rf):
    """Test the response data for an invalid PUT request."""
    url = reverse('eye-django-gen')
    request = rf.put(url)
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert response_data == {"error": "Invalid request method."}

def test_generator_view_delete_request_status_code(rf):
    """Test the status code for an invalid DELETE request."""
    url = reverse('generaeye-django-gentor')
    request = rf.delete(url)
    response = generator_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_generator_view_delete_request_response_type(rf):
    """Test the response type for an invalid DELETE request."""
    url = reverse('eye-django-gen')
    request = rf.delete(url)
    response = generator_view(request)
    assert response['Content-Type'] == 'application/json'

def test_generator_view_delete_request_response_data(rf):
    """Test the response data for an invalid DELETE request."""
    url = reverse('eye-django-gen')
    request = rf.delete(url)
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert response_data == {"error": "Invalid request method."}

def test_generator_view_patch_request_status_code(rf):
    """Test the status code for an invalid PATCH request."""
    url = reverse('eye-django-gen')
    request = rf.patch(url)
    response = generator_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_generator_view_patch_request_response_type(rf):
    """Test the response type for an invalid PATCH request."""
    url = reverse('geneeye-django-genrator')
    request = rf.patch(url)
    response = generator_view(request)
    assert response['Content-Type'] == 'application/json'

def test_generator_view_patch_request_response_data(rf):
    """Test the response data for an invalid PATCH request."""
    url = reverse('eye-django-gen')
    request = rf.patch(url)
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert response_data == {"error": "Invalid request method."}

def test_generator_view_with_allowany_permission_status_code(rf):
    """Test the status code for a POST request with AllowAny permission."""
    url = reverse('eye-django-gen')
    request = rf.post(url)
    response = generator_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_generator_view_with_allowany_permission_response_type(rf):
    """Test the response type for a POST request with AllowAny permission."""
    url = reverse('eye-django-gen')
    request = rf.post(url)
    response = generator_view(request)
    assert response['Content-Type'] == 'application/json'

def test_generator_view_with_allowany_permission_response_data_has_key(rf):
    """Test that the response data contains a 'key' field for a POST request with AllowAny permission."""
    url = reverse('eye-django-gen')
    request = rf.post(url)
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert 'key' in response_data

def test_generator_view_with_allowany_permission_response_data_key_not_empty(rf):
    """Test that the 'key' in the response data is not empty for a POST request with AllowAny permission."""
    url = reverse('eye-django-gen')
    request = rf.post(url)
    response = generator_view(request)
    response_data = json.loads(response.content)
    assert len(response_data['key']) > 0
