import json
import pytest
import allure

from rest_framework import status
from django.http import HttpRequest

from backend.views import secure_random_numbers_view


pytestmark = [allure.feature("Secure Random Numbers API"), pytest.mark.api, pytest.mark.math]


@pytest.fixture
def valid_payload() -> dict:
    return {'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True}


@pytest.fixture
def default_payload() -> dict:
    return {'min_value': 1, 'max_value': 10}


def _post_request(rf: HttpRequest, url: str, data: dict):
    request = rf.post(url, data=data)
    response = secure_random_numbers_view(request)
    response.render()
    return response, json.loads(response.content)


@allure.story("Valid generation requests")
@allure.title("POST /secure-random-numbers returns correctly generated numbers")
@pytest.mark.parametrize(
    "payload_fixture, expected_count",
    [
        ("valid_payload", 5),
        ("default_payload", 1),
    ],
    ids=["full_payload", "default_count"]
)
def test_post_valid_requests(request, rf, api_endpoints, payload_fixture, expected_count):
    url = api_endpoints["secure_random_numbers"]
    payload = request.getfixturevalue(payload_fixture)

    with allure.step(f"Send POST with payload: {payload}"):
        response, json_data = _post_request(rf, url, payload)
    
    with allure.step("Assert status code and list constraints"):
        assert response.status_code == status.HTTP_200_OK
        assert response['Content-Type'] == 'application/json'
        assert 'random_numbers' in json_data
        
        numbers = json_data['random_numbers']
        assert len(numbers) == expected_count, "Length of random_numbers does not match count"
        assert all(payload['min_value'] <= num <= payload['max_value'] for num in numbers), "Numbers out of bounds"


@allure.story("Invalid requests")
@allure.title("POST /secure-random-numbers returns 400 for missing fields")
@pytest.mark.validation
@pytest.mark.parametrize(
    "payload, missing_field",
    [
        ({'max_value': 10, 'count': 5, 'unique': True}, "min_value"),
        ({'min_value': 1, 'count': 5, 'unique': True}, "max_value"),
    ]
)
def test_post_missing_fields(rf, api_endpoints, payload, missing_field):
    url = api_endpoints["secure_random_numbers"]
    with allure.step(f"Send POST without {missing_field}"):
        response, json_data = _post_request(rf, url, payload)
    
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert json_data == {"error": "min_value and max_value are required."}


@allure.story("Invalid requests")
@allure.title("POST /secure-random-numbers returns 400 for structural errors")
@pytest.mark.validation
@pytest.mark.parametrize(
    "payload, expected_error",
    [
        ({'min_value': 1, 'max_value': 10, 'count': 0, 'unique': True}, 'count cannot be less or equal 0'),
        ({'min_value': 1, 'max_value': 10, 'count': 1001, 'unique': True}, 'count cannot be more than 1000'),
        ({'min_value': 'invalid', 'max_value': 'invalid', 'count': 5, 'unique': True}, None),
        ({'min_value': 10, 'max_value': 1, 'count': 5, 'unique': True}, None),
    ]
)
def test_post_invalid_structure(rf, api_endpoints, payload, expected_error):
    url = api_endpoints["secure_random_numbers"]
    with allure.step("Send structurally invalid POST"):
        response, json_data = _post_request(rf, url, payload)
        
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    if expected_error:
        assert json_data == {"error": expected_error}
    else:
        assert "error" in json_data


@allure.story("HTTP method validation")
@allure.title("Invalid HTTP methods return 405 Method Not Allowed")
@pytest.mark.validation
@pytest.mark.parametrize("method", ['get', 'put', 'delete', 'patch'])
def test_invalid_methods(rf, api_endpoints, method):
    url = api_endpoints["secure_random_numbers"]
    request_method = getattr(rf, method)
    request = request_method(url)
    response = secure_random_numbers_view(request)
    
    response.render()
    json_data = json.loads(response.content)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert json_data == {'detail': f'Method "{method.upper()}" not allowed.'}
