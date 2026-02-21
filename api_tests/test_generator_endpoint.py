import json
import pytest
import allure

from rest_framework import status

from backend.views import generator_view


pytestmark = [allure.feature("Key Generator API"), pytest.mark.api, pytest.mark.generator]


@allure.story("Generate Key Operations")
@allure.title("POST /django-ker-generate valid requests")
@pytest.mark.parametrize(
    "scenario",
    ["valid_request", "allowany_permission"],
    ids=["standard", "allowany_explicit"]
)
def test_post_valid_request(rf, api_endpoints, scenario):
    url = api_endpoints["django_ker_generate"]
    with allure.step(f"Send POST request to {url} ({scenario})"):
        request = rf.post(url, content_type="application/json")
        response = generator_view(request)

    with allure.step("Assert status code and response type"):
        assert response.status_code == status.HTTP_200_OK
        assert response['Content-Type'] == 'application/json'

    with allure.step("Assert response contains non-empty 'key'"):
        response_data = json.loads(response.content)
        assert 'key' in response_data
        assert len(response_data['key']) > 0


@allure.story("Method Validation")
@allure.title("Invalid HTTP methods return 405 Method Not Allowed")
@pytest.mark.validation
@pytest.mark.parametrize("method", ['get', 'put', 'delete', 'patch'])
def test_invalid_methods_return_405(rf, api_endpoints, method):
    url = api_endpoints["django_ker_generate"]
    with allure.step(f"Send {method.upper()} request to {url}"):
        request_method = getattr(rf, method)
        request = request_method(url, content_type="application/json")
        response = generator_view(request)

    with allure.step("Assert 405 status code and error message"):
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert response['Content-Type'] == 'text/html; charset=utf-8'
        
        response.render()
        json_data = json.loads(response.content.decode('utf-8'))
        expected_detail = {'detail': f'Method "{method.upper()}" not allowed.'}
        assert json_data == expected_detail
