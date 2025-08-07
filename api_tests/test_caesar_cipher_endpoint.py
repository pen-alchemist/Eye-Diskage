import json
import pytest
import allure

from django.core.exceptions import RequestDataTooBig
from rest_framework import status
from backend.views import caesar_cipher_view


@allure.feature("Caesar Cipher API")
@allure.story("Encrypt text")
class TestCaesarCipherView:

    @pytest.fixture
    def valid_encrypt_payload(self) -> dict:
        """Payload for a valid encryption request."""
        return {'text': 'HELLO', 'shift': '3', 'mode': 'encrypt'}

    @pytest.fixture
    def invalid_shift_payload(self) -> dict:
        """Payload with invalid (non-integer) shift value."""
        return {'text': 'HELLO', 'shift': 'invalid', 'mode': 'encrypt'}

    @pytest.fixture
    def default_payload(self) -> dict:
        """Payload with only text, to test default shift and mode."""
        return {'text': 'HELLO'}

    @allure.title("POST /caesar-cipher with valid encrypt payload returns 200 OK")
    def test_post_valid_encrypt_status_code(self, rf, api_endpoints, valid_encrypt_payload):
        url = api_endpoints["caesar_cipher"]
        with allure.step(f"Send POST request to {url} with payload: {valid_encrypt_payload}"):
            request = rf.post(
                url,
                data=json.dumps(valid_encrypt_payload),
                content_type="application/json"
            )
            response = caesar_cipher_view(request)

        with allure.step("Assert status code is 200 OK"):
            assert response.status_code == status.HTTP_200_OK, f"Expected 200, got {response.status_code}"

    @allure.title("POST /caesar-cipher returns correct encrypted result")
    def test_post_valid_encrypt_response_data(self, rf, api_endpoints, valid_encrypt_payload):
        url = api_endpoints["caesar_cipher"]
        with allure.step("Send POST request and get response"):
            request = rf.post(
                url,
                data=json.dumps(valid_encrypt_payload),
                content_type="application/json"
            )
            response = caesar_cipher_view(request)
            response.render()
            json_data = json.loads(response.content.decode('utf-8'))

        with allure.step("Verify response contains the correct encrypted text"):
            expected = {"result": "KHOOR"}
            assert json_data == expected, f"Expected response {expected}, got {json_data}"

    @allure.title("POST /caesar-cipher with invalid shift returns 400 Bad Request")
    def test_post_invalid_shift_status_code(self, rf, api_endpoints, invalid_shift_payload):
        url = api_endpoints["caesar_cipher"]
        with allure.step(f"Send POST request with invalid shift to {url}"):
            request = rf.post(
                url,
                data=json.dumps(invalid_shift_payload),
                content_type="application/json"
            )
            response = caesar_cipher_view(request)

        with allure.step("Assert status code is 400 Bad Request"):
            assert response.status_code == status.HTTP_400_BAD_REQUEST, f"Expected 400, got {response.status_code}"

    @allure.title("POST /caesar-cipher with invalid shift returns error message")
    def test_post_invalid_shift_response_data(self, rf, api_endpoints, invalid_shift_payload):
        url = api_endpoints["caesar_cipher"]
        with allure.step("Send POST request and get response with invalid shift"):
            request = rf.post(
                url,
                data=json.dumps(invalid_shift_payload),
                content_type="application/json"
            )
            response = caesar_cipher_view(request)
            response.render()
            json_data = json.loads(response.content.decode('utf-8'))

        with allure.step("Verify error message is returned"):
            expected_error = {'error': "Wrong shift type! invalid literal for int() with base 10: 'invalid'"}
            assert json_data == expected_error, f"Expected error message {expected_error}, got {json_data}"

    @allure.title("POST /caesar-cipher with default shift and mode returns 200 OK")
    def test_post_default_shift_and_mode_status_code(self, rf, api_endpoints, default_payload):
        url = api_endpoints["caesar_cipher"]
        with allure.step(f"Send POST request with default payload to {url}"):
            request = rf.post(
                url,
                data=json.dumps(default_payload),
                content_type="application/json"
            )
            response = caesar_cipher_view(request)

        with allure.step("Assert status code is 200 OK"):
            assert response.status_code == status.HTTP_200_OK, f"Expected 200, got {response.status_code}"

    @allure.title("POST /caesar-cipher with default shift and mode returns correct encrypted result")
    def test_post_default_shift_and_mode_response_data(self, rf, api_endpoints, default_payload):
        url = api_endpoints["caesar_cipher"]
        with allure.step("Send POST request and get response"):
            request = rf.post(
                url,
                data=json.dumps(default_payload),
                content_type="application/json"
            )
            response = caesar_cipher_view(request)
            response.render()
            json_data = json.loads(response.content.decode('utf-8'))

        with allure.step("Verify response contains the correct encrypted text"):
            expected = {"result": "KHOOR"}  # Default shift = 3, mode = 'encrypt'
            assert json_data == expected, f"Expected response {expected}, got {json_data}"

    @allure.title("POST /caesar-cipher with too large text raises RequestDataTooBig")
    def test_post_text_size_exceeds_limit_raises(self, rf, api_endpoints):
        url = api_endpoints["caesar_cipher"]
        large_text = "A" * (10 * 1024 * 1024 + 1)  # 10MB + 1 byte
        payload = {'text': large_text, 'shift': '3', 'mode': 'encrypt'}

        with allure.step("Send POST request with payload exceeding size limit and expect exception"):
            with pytest.raises(RequestDataTooBig):
                request = rf.post(
                    url,
                    data=json.dumps(payload),
                    content_type="application/json"
                )
                caesar_cipher_view(request)
