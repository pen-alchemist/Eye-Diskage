import json
import pytest

from django.test import RequestFactory

from rest_framework import status

from backend.views import secure_random_numbers_view


@pytest.fixture
def rf():
    return RequestFactory()

@pytest.fixture
def secure_random_numbers_url():
    return "/api/eye_diskage/secure-random-numbers/"

def test_secure_random_numbers_view_post_valid_status_code(rf, secure_random_numbers_url):
    """Test the status code for a valid POST request."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_secure_random_numbers_view_post_valid_response_type(rf, secure_random_numbers_url):
    """Test the response type for a valid POST request."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_valid_response_contains_random_numbers(rf, secure_random_numbers_url):
    """Test that the response contains 'random_numbers' for a valid POST request."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert 'random_numbers' in json_data

def test_secure_random_numbers_view_post_valid_response_random_numbers_length(rf, secure_random_numbers_url):
    """Test the length of 'random_numbers' for a valid POST request."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert len(json_data['random_numbers']) == 5

def test_secure_random_numbers_view_post_valid_response_random_numbers_range(rf, secure_random_numbers_url):
    """Test that all numbers in 'random_numbers' are within the valid range for a valid POST request."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert all(1 <= num <= 10 for num in json_data['random_numbers'])

def test_secure_random_numbers_view_post_default_count_and_unique_status_code(rf, secure_random_numbers_url):
    """Test the status code for a POST request with default count and unique values."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10})
    response = secure_random_numbers_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_secure_random_numbers_view_post_default_count_and_unique_response_type(rf, secure_random_numbers_url):
    """Test the response type for a POST request with default count and unique values."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10})
    response = secure_random_numbers_view(request)
    response.render()
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_default_count_and_unique_response_contains_random_numbers(rf, secure_random_numbers_url):
    """Test that the response contains 'random_numbers' for a POST request with default count and unique values."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10})
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert 'random_numbers' in json_data

def test_secure_random_numbers_view_post_default_count_and_unique_response_random_numbers_length(rf, secure_random_numbers_url):
    """Test the length of 'random_numbers' for a POST request with default count and unique values."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10})
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert len(json_data['random_numbers']) == 1  # Default count is 1

def test_secure_random_numbers_view_post_default_count_and_unique_response_random_numbers_range(rf, secure_random_numbers_url):
    """Test that all numbers in 'random_numbers' are within the valid range for a POST request with default count and unique values."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10})
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert all(1 <= num <= 10 for num in json_data['random_numbers'])

def test_secure_random_numbers_view_post_missing_min_value_status_code(rf, secure_random_numbers_url):
    """Test the status code for a POST request with a missing min_value."""
    request = rf.post(secure_random_numbers_url, data={'max_value': 10, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_missing_min_value_response_type(rf, secure_random_numbers_url):
    """Test the response type for a POST request with a missing min_value."""
    request = rf.post(secure_random_numbers_url, data={'max_value': 10, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_missing_min_value_response_data(rf, secure_random_numbers_url):
    """Test the response data for a POST request with a missing min_value."""
    request = rf.post(secure_random_numbers_url, data={'max_value': 10, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {"error": "min_value and max_value are required."}

def test_secure_random_numbers_view_post_missing_max_value_status_code(rf, secure_random_numbers_url):
    """Test the status code for a POST request with a missing max_value."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_missing_max_value_response_type(rf, secure_random_numbers_url):
    """Test the response type for a POST request with a missing max_value."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_missing_max_value_response_data(rf, secure_random_numbers_url):
    """Test the response data for a POST request with a missing max_value."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {"error": "min_value and max_value are required."}

def test_secure_random_numbers_view_post_invalid_count_status_code(rf, secure_random_numbers_url):
    """Test the status code for a POST request with an invalid count."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 0, 'unique': True})
    response = secure_random_numbers_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_invalid_count_response_type(rf, secure_random_numbers_url):
    """Test the response type for a POST request with an invalid count."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 0, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_invalid_count_response_data(rf, secure_random_numbers_url):
    """Test the response data for a POST request with an invalid count."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 0, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {'error': 'count cannot be less or equal 0'}

def test_secure_random_numbers_view_post_count_exceeds_limit_status_code(rf, secure_random_numbers_url):
    """Test the status code for a POST request with a count exceeding the limit."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 1001, 'unique': True})
    response = secure_random_numbers_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_count_exceeds_limit_response_type(rf, secure_random_numbers_url):
    """Test the response type for a POST request with a count exceeding the limit."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 1001, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_count_exceeds_limit_response_data(rf, secure_random_numbers_url):
    """Test the response data for a POST request with a count exceeding the limit."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 1001, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {"error": "count cannot be more than 1000"}

def test_secure_random_numbers_view_post_invalid_min_max_values_status_code(rf, secure_random_numbers_url):
    """Test the status code for a POST request with invalid min_value and max_value."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 'invalid', 'max_value': 'invalid', 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_invalid_min_max_values_response_type(rf, secure_random_numbers_url):
    """Test the response type for a POST request with invalid min_value and max_value."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 'invalid', 'max_value': 'invalid', 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_invalid_min_max_values_response_data(rf, secure_random_numbers_url):
    """Test the response data for a POST request with invalid min_value and max_value."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 'invalid', 'max_value': 'invalid', 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert "error" in json_data

def test_secure_random_numbers_view_post_min_value_greater_than_max_value_status_code(rf, secure_random_numbers_url):
    """Test the status code for a POST request with min_value greater than max_value."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 10, 'max_value': 1, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_secure_random_numbers_view_post_min_value_greater_than_max_value_response_type(rf, secure_random_numbers_url):
    """Test the response type for a POST request with min_value greater than max_value."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 10, 'max_value': 1, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_min_value_greater_than_max_value_response_data(rf, secure_random_numbers_url):
    """Test the response data for a POST request with min_value greater than max_value."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 10, 'max_value': 1, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert "error" in json_data

def test_secure_random_numbers_view_post_get_request_status_code(rf, secure_random_numbers_url):
    """Test the status code for an invalid GET request."""
    request = rf.get(secure_random_numbers_url)
    response = secure_random_numbers_view(request)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_secure_random_numbers_view_post_get_request_response_type(rf, secure_random_numbers_url):
    """Test the response type for an invalid GET request."""
    request = rf.get(secure_random_numbers_url)
    response = secure_random_numbers_view(request)
    response.render()
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_get_request_response_data(rf, secure_random_numbers_url):
    """Test the response data for an invalid GET request."""
    request = rf.get(secure_random_numbers_url)
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {'detail': 'Method "GET" not allowed.'}

def test_secure_random_numbers_view_post_put_request_status_code(rf, secure_random_numbers_url):
    """Test the status code for an invalid PUT request."""
    request = rf.put(secure_random_numbers_url)
    response = secure_random_numbers_view(request)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_secure_random_numbers_view_post_put_request_response_type(rf, secure_random_numbers_url):
    """Test the response type for an invalid PUT request."""
    request = rf.put(secure_random_numbers_url)
    response = secure_random_numbers_view(request)
    response.render()
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_put_request_response_data(rf, secure_random_numbers_url):
    """Test the response data for an invalid PUT request."""
    request = rf.put(secure_random_numbers_url)
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {'detail': 'Method "PUT" not allowed.'}

def test_secure_random_numbers_view_post_delete_request_status_code(rf, secure_random_numbers_url):
    """Test the status code for an invalid DELETE request."""
    request = rf.delete(secure_random_numbers_url)
    response = secure_random_numbers_view(request)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_secure_random_numbers_view_post_delete_request_response_type(rf, secure_random_numbers_url):
    """Test the response type for an invalid DELETE request."""
    request = rf.delete(secure_random_numbers_url)
    response = secure_random_numbers_view(request)
    response.render()
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_delete_request_response_data(rf, secure_random_numbers_url):
    """Test the response data for an invalid DELETE request."""
    request = rf.delete(secure_random_numbers_url)
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {'detail': 'Method "DELETE" not allowed.'}

def test_secure_random_numbers_view_post_patch_request_status_code(rf, secure_random_numbers_url):
    """Test the status code for an invalid PATCH request."""
    request = rf.patch(secure_random_numbers_url)
    response = secure_random_numbers_view(request)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

def test_secure_random_numbers_view_post_patch_request_response_type(rf, secure_random_numbers_url):
    """Test the response type for an invalid PATCH request."""
    request = rf.patch(secure_random_numbers_url)
    response = secure_random_numbers_view(request)
    response.render()
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_post_patch_request_response_data(rf, secure_random_numbers_url):
    """Test the response data for an invalid PATCH request."""
    request = rf.patch(secure_random_numbers_url)
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert json_data == {'detail': 'Method "PATCH" not allowed.'}

def test_secure_random_numbers_view_with_allowany_permission_status_code(rf, secure_random_numbers_url):
    """Test the status code for a POST request with AllowAny permission."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    assert response.status_code == status.HTTP_200_OK

def test_secure_random_numbers_view_with_allowany_permission_response_type(rf, secure_random_numbers_url):
    """Test the response type for a POST request with AllowAny permission."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    assert response['Content-Type'] == 'application/json'

def test_secure_random_numbers_view_with_allowany_permission_response_contains_random_numbers(rf, secure_random_numbers_url):
    """Test that the response contains 'random_numbers' for a POST request with AllowAny permission."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert 'random_numbers' in json_data

def test_secure_random_numbers_view_with_allowany_permission_response_random_numbers_length(rf, secure_random_numbers_url):
    """Test the length of 'random_numbers' for a POST request with AllowAny permission."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert len(json_data['random_numbers']) == 5

def test_secure_random_numbers_view_with_allowany_permission_response_random_numbers_range(rf, secure_random_numbers_url):
    """Test that all numbers in 'random_numbers' are within the valid range for a POST request with AllowAny permission."""
    request = rf.post(secure_random_numbers_url, data={'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True})
    response = secure_random_numbers_view(request)
    response.render()
    json_data = json.loads(response.content.decode('utf-8'))
    assert all(1 <= num <= 10 for num in json_data['random_numbers'])
