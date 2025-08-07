import json
import pytest
import allure

from rest_framework import status
from backend.views import generator_view


@allure.feature("Key Generator API")
@allure.story("Generate key endpoint")
class TestGeneratorView:

    @pytest.fixture
    def url(self, api_endpoints):
        """API endpoint URL for the key generator."""
        return api_endpoints["django_ker_generate"]

    @allure.title("POST /django-ker-generate returns 200 OK with valid response")
    def test_post_valid_request_status_code_and_response(self, rf, url):
        with allure.step(f"Send POST request to {url}"):
            request = rf.post(url, content_type="application/json")
            response = generator_view(request)

        with allure.step("Assert status code is 200 OK"):
            assert response.status_code == status.HTTP_200_OK, f"Expected 200, got {response.status_code}"

        with allure.step("Assert response content type is application/json"):
            assert response['Content-Type'] == 'application/json', f"Expected 'application/json', got {response['Content-Type']}"

        with allure.step("Assert response contains 'key' field which is non-empty"):
            response_data = json.loads(response.content)
            assert 'key' in response_data, "'key' field missing in response"
            assert len(response_data['key']) > 0, "'key' field is empty"

    @pytest.mark.parametrize("method", ['get', 'put', 'delete', 'patch'])
    @allure.title("Invalid HTTP methods return 405 Method Not Allowed")
    def test_invalid_methods_return_405(self, rf, url, method):
        with allure.step(f"Send {method.upper()} request to {url}"):
            request_method = getattr(rf, method)
            request = request_method(url, content_type="application/json")
            response = generator_view(request)

        with allure.step("Assert status code is 405 Method Not Allowed"):
            assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED, f"Expected 405, got {response.status_code}"

        with allure.step("Assert response content type is text/html; charset=utf-8"):
            assert response['Content-Type'] == 'text/html; charset=utf-8', f"Expected 'text/html; charset=utf-8', got {response['Content-Type']}"

        with allure.step("Assert response JSON error message"):
            response.render()
            json_data = json.loads(response.content.decode('utf-8'))
            expected_detail = {'detail': f'Method "{method.upper()}" not allowed.'}
            assert json_data == expected_detail, f"Expected {expected_detail}, got {json_data}"

    @allure.title("POST /django-ker-generate respects AllowAny permission and returns valid key")
    def test_post_with_allowany_permission(self, rf, url):
        # This test duplicates the POST test above but is kept for explicit permission check as per original.
        with allure.step(f"Send POST request with AllowAny permission to {url}"):
            request = rf.post(url, content_type="application/json")
            response = generator_view(request)

        with allure.step("Assert status code is 200 OK"):
            assert response.status_code == status.HTTP_200_OK, f"Expected 200, got {response.status_code}"

        with allure.step("Assert response content type is application/json"):
            assert response['Content-Type'] == 'application/json', f"Expected 'application/json', got {response['Content-Type']}"

        with allure.step("Assert response contains 'key' field which is non-empty"):
            response_data = json.loads(response.content)
            assert 'key' in response_data, "'key' field missing in response"
            assert len(response_data['key']) > 0, "'key' field is empty"
