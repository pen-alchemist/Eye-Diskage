import pytest

from django.test import Client
from django.urls import reverse

from rest_framework import status


@pytest.fixture
def client_django():
    return Client()

def test_secure_random_numbers_view_post_valid_status_code(client_django):
    """Test the status code for a valid POST request."""
    url = reverse('eye-secure-numbers')  # Ensure the correct URL name is used
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    assert response.status_code == status.HTTP_200_OK

def test_secure_random_numbers_view_post_valid_response_type(client_django):
    """Test the response type for a valid POST request."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_valid_response_contains_random_numbers(client_django):
    """Test that the response contains 'random_numbers' for a valid POST request."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response_data = response.json()
    assert 'random_numbers' in response_data

def test_secure_random_numbers_view_post_valid_response_random_numbers_length(client_django):
    """Test the length of 'random_numbers' for a valid POST request."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response_data = response.json()
    assert len(response_data['random_numbers']) == 5

def test_secure_random_numbers_view_post_valid_response_random_numbers_range(client_django):
    """Test that all numbers in 'random_numbers' are within the valid range for a valid POST request."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response_data = response.json()
    assert all(1 <= num <= 10 for num in response_data['random_numbers'])

def test_secure_random_numbers_view_post_default_count_and_unique_status_code(client_django):
    """Test the status code for a POST request with default count and unique values."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10})
    assert response.status_code == status.HTTP_200_OK

def test_secure_random_numbers_view_post_default_count_and_unique_response_type(client_django):
    """Test the response type for a POST request with default count and unique values."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10})
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_default_count_and_unique_response_contains_random_numbers(client_django):
    """Test that the response contains 'random_numbers' for a POST request with default count and unique values."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10})
    response_data = response.json()
    assert 'random_numbers' in response_data

def test_secure_random_numbers_view_post_default_count_and_unique_response_random_numbers_length(client_django):
    """Test the length of 'random_numbers' for a POST request with default count and unique values."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10})
    response_data = response.json()
    assert len(response_data['random_numbers']) == 1  # Default count is 1

def test_secure_random_numbers_view_post_default_count_and_unique_response_random_numbers_range(client_django):
    """Test that all numbers in 'random_numbers' are within the valid range for a POST request with default count and unique values."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10})
    response_data = response.json()
    assert all(1 <= num <= 10 for num in response_data['random_numbers'])

def test_secure_random_numbers_view_post_missing_min_value_status_code(client_django):
    """Test the status code for a POST request with a missing min_value."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'max_value': 10, 'count': 5, 'unique': True})
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_missing_min_value_response_type(client_django):
    """Test the response type for a POST request with a missing min_value."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'max_value': 10, 'count': 5, 'unique': True})
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_missing_min_value_response_data(client_django):
    """Test the response data for a POST request with a missing min_value."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'max_value': 10, 'count': 5, 'unique': True})
    response_data = response.json()
    assert response_data == {"error": "min_value and max_value are required."}

def test_secure_random_numbers_view_post_missing_max_value_status_code(client_django):
    """Test the status code for a POST request with a missing max_value."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'count': 5, 'unique': True})
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_missing_max_value_response_type(client_django):
    """Test the response type for a POST request with a missing max_value."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'count': 5, 'unique': True})
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_missing_max_value_response_data(client_django):
    """Test the response data for a POST request with a missing max_value."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'count': 5, 'unique': True})
    response_data = response.json()
    assert response_data == {"error": "min_value and max_value are required."}

def test_secure_random_numbers_view_post_invalid_count_status_code(client_django):
    """Test the status code for a POST request with an invalid count."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 0, 'unique': True})
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_invalid_count_response_type(client_django):
    """Test the response type for a POST request with an invalid count."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 0, 'unique': True})
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_invalid_count_response_data(client_django):
    """Test the response data for a POST request with an invalid count."""
    url = reverse('secure-random-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 0, 'unique': True})
    response_data = response.json()
    assert response_data == {"error": "count cannot be less or equal 0"}

def test_secure_random_numbers_view_post_count_exceeds_limit_status_code(client_django):
    """Test the status code for a POST request with a count exceeding the limit."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 1001, 'unique': True})
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_count_exceeds_limit_response_type(client_django):
    """Test the response type for a POST request with a count exceeding the limit."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 1001, 'unique': True})
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_count_exceeds_limit_response_data(client_django):
    """Test the response data for a POST request with a count exceeding the limit."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 1001, 'unique': True})
    response_data = response.json()
    assert response_data == {"error": "count cannot be more than 1000"}

def test_secure_random_numbers_view_post_invalid_min_max_values_status_code(client_django):
    """Test the status code for a POST request with invalid min_value and max_value."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 'invalid', 'max_value': 'invalid', 'count': 5, 'unique': True})
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_invalid_min_max_values_response_type(client_django):
    """Test the response type for a POST request with invalid min_value and max_value."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 'invalid', 'max_value': 'invalid', 'count': 5, 'unique': True})
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_invalid_min_max_values_response_data(client_django):
    """Test the response data for a POST request with invalid min_value and max_value."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 'invalid', 'max_value': 'invalid', 'count': 5, 'unique': True})
    response_data = response.json()
    assert "error" in response_data

def test_secure_random_numbers_view_post_min_value_greater_than_max_value_status_code(client_django):
    """Test the status code for a POST request with min_value greater than max_value."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 10, 'max_value': 1, 'count': 5, 'unique': True})
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_min_value_greater_than_max_value_response_type(client_django):
    """Test the response type for a POST request with min_value greater than max_value."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 10, 'max_value': 1, 'count': 5, 'unique': True})
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_min_value_greater_than_max_value_response_data(client_django):
    """Test the response data for a POST request with min_value greater than max_value."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 10, 'max_value': 1, 'count': 5, 'unique': True})
    response_data = response.json()
    assert "error" in response_data

def test_secure_random_numbers_view_post_get_request_status_code(client_django):
    """Test the status code for an invalid GET request."""
    url = reverse('eye-secure-numbers')
    response = client_django.get(url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_get_request_response_type(client_django):
    """Test the response type for an invalid GET request."""
    url = reverse('eye-secure-numbers')
    response = client_django.get(url)
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_get_request_response_data(client_django):
    """Test the response data for an invalid GET request."""
    url = reverse('eye-secure-numbers')
    response = client_django.get(url)
    response_data = response.json()
    assert response_data == {"error": "Invalid request method."}

def test_secure_random_numbers_view_post_put_request_status_code(client_django):
    """Test the status code for an invalid PUT request."""
    url = reverse('eye-secure-numbers')
    response = client_django.put(url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_put_request_response_type(client_django):
    """Test the response type for an invalid PUT request."""
    url = reverse('eye-secure-numbers')
    response = client_django.put(url)
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_put_request_response_data(client_django):
    """Test the response data for an invalid PUT request."""
    url = reverse('eye-secure-numbers')
    response = client_django.put(url)
    response_data = response.json()
    assert response_data == {"error": "Invalid request method."}

def test_secure_random_numbers_view_post_delete_request_status_code(client_django):
    """Test the status code for an invalid DELETE request."""
    url = reverse('eye-secure-numbers')
    response = client_django.delete(url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_delete_request_response_type(client_django):
    """Test the response type for an invalid DELETE request."""
    url = reverse('eye-secure-numbers')
    response = client_django.delete(url)
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_delete_request_response_data(client_django):
    """Test the response data for an invalid DELETE request."""
    url = reverse('eye-secure-numbers')
    response = client_django.delete(url)
    response_data = response.json()
    assert response_data == {"error": "Invalid request method."}

def test_secure_random_numbers_view_post_patch_request_status_code(client_django):
    """Test the status code for an invalid PATCH request."""
    url = reverse('eye-secure-numbers')
    response = client_django.patch(url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_patch_request_response_type(client_django):
    """Test the response type for an invalid PATCH request."""
    url = reverse('eye-secure-numbers')
    response = client_django.patch(url)
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_patch_request_response_data(client_django):
    """Test the response data for an invalid PATCH request."""
    url = reverse('eye-secure-numbers')
    response = client_django.patch(url)
    response_data = response.json()
    assert response_data == {"error": "Invalid request method."}

def test_secure_random_numbers_view_with_allowany_permission_status_code(client_django):
    """Test the status code for a POST request with AllowAny permission."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    assert response.status_code == status.HTTP_200_OK

def test_secure_random_numbers_view_with_allowany_permission_response_type(client_django):
    """Test the response type for a POST request with AllowAny permission."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_with_allowany_permission_response_contains_random_numbers(client_django):
    """Test that the response contains 'random_numbers' for a POST request with AllowAny permission."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response_data = response.json()
    assert 'random_numbers' in response_data

def test_secure_random_numbers_view_with_allowany_permission_response_random_numbers_length(client_django):
    """Test the length of 'random_numbers' for a POST request with AllowAny permission."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response_data = response.json()
    assert len(response_data['random_numbers']) == 5

def test_secure_random_numbers_view_with_allowany_permission_response_random_numbers_range(client_django):
    """Test that all numbers in 'random_numbers' are within the valid range for a POST request with AllowAny permission."""
    url = reverse('eye-secure-numbers')
    response = client_django.post(url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response_data = response.json()
    assert all(1 <= num <= 10 for num in response_data['random_numbers'])
