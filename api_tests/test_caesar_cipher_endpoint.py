import json
import pytest
import allure

from django.core.exceptions import RequestDataTooBig
from rest_framework import status

from backend.views import caesar_cipher_view


pytestmark = [allure.feature("Caesar Cipher API"), pytest.mark.api, pytest.mark.crypto]


@pytest.fixture
def valid_encrypt_payload() -> dict:
    return {'text': 'HELLO', 'shift': '3', 'mode': 'encrypt'}


@pytest.fixture
def invalid_shift_payload() -> dict:
    return {'text': 'HELLO', 'shift': 'invalid', 'mode': 'encrypt'}


@pytest.fixture
def default_payload() -> dict:
    return {'text': 'HELLO'}


@allure.story("Encryption Operations")
@allure.title("POST /caesar-cipher with valid payloads")
@pytest.mark.parametrize(
    "payload_fixture, expected_status, expected_result",
    [
        ("valid_encrypt_payload", status.HTTP_200_OK, {"result": "KHOOR"}),
        ("default_payload", status.HTTP_200_OK, {"result": "KHOOR"}),
    ],
    ids=["valid_encrypt", "default_shift"]
)
def test_post_valid_encrypt(request, rf, api_endpoints, payload_fixture, expected_status, expected_result):
    url = api_endpoints["caesar_cipher"]
    payload = request.getfixturevalue(payload_fixture)

    with allure.step(f"Send POST request to {url} with {payload}"):
        req = rf.post(url, data=json.dumps(payload), content_type="application/json")
        response = caesar_cipher_view(req)

    with allure.step("Assert status code and response data"):
        assert response.status_code == expected_status
        
        response.render()
        json_data = json.loads(response.content.decode('utf-8'))
        assert json_data == expected_result


@allure.story("Validation Handling")
@allure.title("POST /caesar-cipher with invalid shift")
@pytest.mark.validation
def test_post_invalid_shift(rf, api_endpoints, invalid_shift_payload):
    url = api_endpoints["caesar_cipher"]
    with allure.step(f"Send POST request to {url} with invalid shift"):
        request = rf.post(
            url,
            data=json.dumps(invalid_shift_payload),
            content_type="application/json"
        )
        response = caesar_cipher_view(request)

    with allure.step("Assert 400 Bad Request and error message"):
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        response.render()
        json_data = json.loads(response.content.decode('utf-8'))
        expected_error = {'error': "Wrong shift type! invalid literal for int() with base 10: 'invalid'"}
        assert json_data == expected_error


@allure.story("Security and Limitations")
@allure.title("POST /caesar-cipher with huge text raises RequestDataTooBig")
@pytest.mark.security
def test_post_text_size_exceeds_limit(rf, api_endpoints):
    url = api_endpoints["caesar_cipher"]
    large_text = "A" * (10 * 1024 * 1024 + 1)  # 10MB + 1 byte
    payload = {'text': large_text, 'shift': '3', 'mode': 'encrypt'}

    with allure.step("Send oversized payload and assert RequestDataTooBig"):
        with pytest.raises(RequestDataTooBig):
            request = rf.post(
                url,
                data=json.dumps(payload),
                content_type="application/json"
            )
            caesar_cipher_view(request)
