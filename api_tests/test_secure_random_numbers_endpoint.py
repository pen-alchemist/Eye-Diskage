import json
import pytest
import allure

from rest_framework import status
from django.http import HttpRequest

from backend.views import secure_random_numbers_view


@allure.feature("Secure Random Numbers API")
class TestSecureRandomNumbersView:
    @pytest.fixture
    def valid_payload(self) -> dict:
        return {'min_value': 1, 'max_value': 10, 'count': 5, 'unique': True}

    @pytest.fixture
    def default_payload(self) -> dict:
        return {'min_value': 1, 'max_value': 10}

    def _post_request(self, rf: HttpRequest, url: str, data: dict):
        request = rf.post(url, data=data)
        response = secure_random_numbers_view(request)
        response.render()
        return response, json.loads(response.content)

    @allure.story("Valid requests")
    @allure.title("Valid POST returns 200 and correct data structure")
    def test_post_valid(self, rf, secure_random_numbers_url, valid_payload):
        response, json_data = self._post_request(rf, secure_random_numbers_url, valid_payload)
        assert response.status_code == status.HTTP_200_OK, "Expected status 200 OK"
        assert response['Content-Type'] == 'application/json', "Expected Content-Type application/json"
        assert 'random_numbers' in json_data, "'random_numbers' key missing in response"
        assert len(json_data['random_numbers']) == valid_payload['count'], "Length of random_numbers does not match count"
        assert all(valid_payload['min_value'] <= num <= valid_payload['max_value'] for num in json_data['random_numbers']), "Random numbers out of specified range"

    @allure.story("Valid requests")
    @allure.title("POST with default count and unique returns 200 and correct data")
    def test_post_default_count_unique(self, rf, secure_random_numbers_url, default_payload):
        response, json_data = self._post_request(rf, secure_random_numbers_url, default_payload)
        assert response.status_code == status.HTTP_200_OK, "Expected status 200 OK"
        assert response['Content-Type'] == 'application/json', "Expected Content-Type application/json"
        assert 'random_numbers' in json_data, "'random_numbers' key missing in response"
        assert len(json_data['random_numbers']) == 1, "Default count expected to be 1"
        assert all(default_payload['min_value'] <= num <= default_payload['max_value'] for num in json_data['random_numbers']), "Random numbers out of specified range"

    @allure.story("Invalid requests - missing parameters")
    @pytest.mark.parametrize(
        "payload, missing_field",
        [
            ({'max_value': 10, 'count': 5, 'unique': True}, "min_value"),
            ({'min_value': 1, 'count': 5, 'unique': True}, "max_value"),
        ]
    )
    @allure.title("POST missing required fields returns 400 with error")
    def test_post_missing_fields(self, rf, secure_random_numbers_url, payload, missing_field):
        response, json_data = self._post_request(rf, secure_random_numbers_url, payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST, f"Expected 400 Bad Request when missing {missing_field}"
        assert response['Content-Type'] == 'application/json'
        assert json_data == {"error": "min_value and max_value are required."}

    @allure.story("Invalid requests - invalid count")
    @pytest.mark.parametrize(
        "payload, expected_error",
        [
            ({'min_value': 1, 'max_value': 10, 'count': 0, 'unique': True}, 'count cannot be less or equal 0'),
            ({'min_value': 1, 'max_value': 10, 'count': 1001, 'unique': True}, 'count cannot be more than 1000'),
        ]
    )
    @allure.title("POST invalid count returns 400 with error")
    def test_post_invalid_count(self, rf, secure_random_numbers_url, payload, expected_error):
        response, json_data = self._post_request(rf, secure_random_numbers_url, payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response['Content-Type'] == 'application/json'
        assert json_data == {"error": expected_error}

    @allure.story("Invalid requests - invalid min/max")
    @pytest.mark.parametrize(
        "payload",
        [
            {'min_value': 'invalid', 'max_value': 'invalid', 'count': 5, 'unique': True},
            {'min_value': 10, 'max_value': 1, 'count': 5, 'unique': True},  # min_value > max_value
        ]
    )
    @allure.title("POST invalid min/max values returns 400 with error")
    def test_post_invalid_min_max(self, rf, secure_random_numbers_url, payload):
        response, json_data = self._post_request(rf, secure_random_numbers_url, payload)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response['Content-Type'] == 'application/json'
        assert "error" in json_data

    @allure.story("HTTP method validation")
    @pytest.mark.parametrize(
        "method",
        ['get', 'put', 'delete', 'patch']
    )
    @allure.title("Invalid HTTP methods return 405 Method Not Allowed")
    def test_invalid_methods(self, rf, secure_random_numbers_url, method):
        request_method = getattr(rf, method)
        request = request_method(secure_random_numbers_url)
        response = secure_random_numbers_view(request)
        response.render()
        json_data = json.loads(response.content)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert response['Content-Type'] == 'application/json'
        assert json_data == {'detail': f'Method "{method.upper()}" not allowed.'}

    @allure.story("Permission tests")
    @allure.title("POST request with AllowAny permission returns 200 with expected data")
    def test_post_allow_any_permission(self, rf, secure_random_numbers_url, valid_payload):
        response, json_data = self._post_request(rf, secure_random_numbers_url, valid_payload)
        assert response.status_code == status.HTTP_200_OK
        assert response['Content-Type'] == 'application/json'
        assert 'random_numbers' in json_data
        assert len(json_data['random_numbers']) == valid_payload['count']
        assert all(valid_payload['min_value'] <= num <= valid_payload['max_value'] for num in json_data['random_numbers'])
