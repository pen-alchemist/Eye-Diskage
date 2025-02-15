import json
import pytest

from django.test import Client
from django.urls import reverse

from rest_framework import status


@pytest.fixture
def client_django():
    return Client()

def test_generator_view_post_valid_request_status_code(client_django):
    """Test the status code for a valid POST request."""
    url = reverse('eye-django-gen')  # Ensure the correct URL name is used
    response = client_django.post(url)
    assert response.status_code == status.HTTP_200_OK

def test_generator_view_post_valid_request_response_type(client_django):
    """Test the response type for a valid POST request."""
    url = reverse('eye-django-gen')
    response = client_django.post(url)
    assert response['Content-Type'] == 'application/json'

def test_generator_view_post_valid_request_response_data_has_key(client_django):
    """Test that the response data contains a 'key' field for a valid POST request."""
    url = reverse('eye-django-gen')
    response = client_django.post(url)
    response_data = json.loads(response.content)
    assert 'key' in response_data

def test_generator_view_post_valid_request_response_data_key_not_empty(client_django):
    """Test that the 'key' in the response data is not empty for a valid POST request."""
    url = reverse('eye-django-gen')
    response = client_django.post(url)
    response_data = json.loads(response.content)
    assert len(response_data['key']) > 0

def test_generator_view_get_request_response_type(client_django):
    """Test the response type for an invalid GET request."""
    url = reverse('eye-django-gen')
    response = client_django.get(url)
    assert response['Content-Type'] == 'application/json'

def test_generator_view_get_request_response_data(client_django):
    """Test the response data for an invalid GET request."""
    url = reverse('eye-django-gen')
    response = client_django.get(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_generator_view_put_request_status_code(client_django):
    """Test the status code for an invalid PUT request."""
    url = reverse('eye-django-gen')
    response = client_django.put(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_generator_view_put_request_response_type(client_django):
    """Test the response type for an invalid PUT request."""
    url = reverse('eye-django-gen')
    response = client_django.put(url)
    assert response['Content-Type'] == 'application/json'

def test_generator_view_put_request_response_data(client_django):
    """Test the response data for an invalid PUT request."""
    url = reverse('eye-django-gen')
    response = client_django.put(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_generator_view_delete_request_status_code(client_django):
    """Test the status code for an invalid DELETE request."""
    url = reverse('eye-django-gen')
    response = client_django.delete(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_generator_view_delete_request_response_type(client_django):
    """Test the response type for an invalid DELETE request."""
    url = reverse('eye-django-gen')
    response = client_django.delete(url)
    assert response['Content-Type'] == 'application/json'

def test_generator_view_delete_request_response_data(client_django):
    """Test the response data for an invalid DELETE request."""
    url = reverse('eye-django-gen')
    response = client_django.delete(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_generator_view_patch_request_status_code(client_django):
    """Test the status code for an invalid PATCH request."""
    url = reverse('eye-django-gen')
    response = client_django.patch(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_generator_view_patch_request_response_type(client_django):
    """Test the response type for an invalid PATCH request."""
    url = reverse('eye-django-gen')
    response = client_django.patch(url)
    assert response['Content-Type'] == 'application/json'

def test_generator_view_patch_request_response_data(client_django):
    """Test the response data for an invalid PATCH request."""
    url = reverse('eye-django-gen')
    response = client_django.patch(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_generator_view_with_allowany_permission_status_code(client_django):
    """Test the status code for a POST request with AllowAny permission."""
    url = reverse('eye-django-gen')
    response = client_django.post(url)
    assert response.status_code == status.HTTP_200_OK

def test_generator_view_with_allowany_permission_response_type(client_django):
    """Test the response type for a POST request with AllowAny permission."""
    url = reverse('eye-django-gen')
    response = client_django.post(url)
    assert response['Content-Type'] == 'application/json'

def test_generator_view_with_allowany_permission_response_data_has_key(client_django):
    """Test that the response data contains a 'key' field for a POST request with AllowAny permission."""
    url = reverse('eye-django-gen')
    response = client_django.post(url)
    response_data = json.loads(response.content)
    assert 'key' in response_data

def test_generator_view_with_allowany_permission_response_data_key_not_empty(client_django):
    """Test that the 'key' in the response data is not empty for a POST request with AllowAny permission."""
    url = reverse('eye-django-gen')
    response = client_django.post(url)
    response_data = json.loads(response.content)
    assert len(response_data['key']) > 0
