import json
import pytest
import allure

from rest_framework import status
from django.core.exceptions import RequestDataTooBig

from backend.views import vigenere_cipher_view


pytestmark = [allure.feature("Vigenere Cipher API"), pytest.mark.api, pytest.mark.crypto]


@allure.story("Encryption and Decryption Operations")
@allure.title("POST /vigenere-cipher responses based on payload")
@pytest.mark.parametrize(
    "payload, expected_status, expected_response",
    [
        ({"text": "HELLO", "key": "KEY", "mode": "encrypt"}, status.HTTP_200_OK, {"result": "RIJVS"}),
        ({"text": "RIJVS", "key": "KEY", "mode": "decrypt"}, status.HTTP_200_OK, {"result": "HELLO"}),
        ({"text": "HELLO", "mode": "encrypt"}, status.HTTP_400_BAD_REQUEST, {"error": "Key is required."}),
        ({"text": "HELLO", "key": "", "mode": "encrypt"}, status.HTTP_400_BAD_REQUEST, {"error": "Key is required."}),
        ({"text": "HELLO", "key": "KEY", "mode": "invalid_mode"}, status.HTTP_200_OK, None),
    ],
    ids=[
        "valid_encrypt",
        "valid_decrypt",
        "missing_key",
        "empty_key",
        "invalid_mode"
    ]
)
def test_vigenere_cipher_post_requests(rf, api_endpoints, payload, expected_status, expected_response):
    url = api_endpoints["vigenere_cipher"]
    with allure.step(f"Send POST request to {url} with payload {payload}"):
        request = rf.post(url, data=payload)
        response = vigenere_cipher_view(request)

    with allure.step(f"Assert status code is {expected_status}"):
        assert response.status_code == expected_status
        assert response["Content-Type"] == "text/html; charset=utf-8"
    
    with allure.step("Assert response JSON matches expected"):
        response.render()
        json_data = json.loads(response.content.decode("utf-8"))

        if expected_response is not None:
            assert json_data == expected_response
        else:
            assert "result" in json_data


@allure.story("Security and Limitations")
@allure.title("POST /vigenere-cipher with excessively large text raises RequestDataTooBig")
@pytest.mark.security
def test_vigenere_cipher_view_text_size_limit(rf, api_endpoints):
    url = api_endpoints["vigenere_cipher"]
    large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
    with allure.step("Send oversized payload and assert RequestDataTooBig is raised"):
        with pytest.raises(RequestDataTooBig):
            request = rf.post(url, data={"text": large_text, "key": "KEY", "mode": "encrypt"})
            vigenere_cipher_view(request)


@allure.story("Method Validation")
@allure.title("Invalid HTTP methods return 405 Method Not Allowed")
@pytest.mark.validation
@pytest.mark.parametrize("method", ["get", "put", "delete", "patch"])
def test_vigenere_cipher_view_disallowed_methods(rf, api_endpoints, method):
    url = api_endpoints["vigenere_cipher"]
    with allure.step(f"Send {method.upper()} request to {url}"):
        request_method = getattr(rf, method)
        request = request_method(url)
        response = vigenere_cipher_view(request)

    with allure.step("Assert status code is 405"):
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        assert response["Content-Type"] == "text/html; charset=utf-8"
        
        response.render()
        json_data = json.loads(response.content.decode("utf-8"))
        assert json_data == {'detail': f'Method "{method.upper()}" not allowed.'}


@allure.story("Permission Tests")
@allure.title("POST /vigenere-cipher respects AllowAny permission")
@pytest.mark.parametrize(
    "data, expected_result",
    [
        ({"text": "HELLO", "key": "KEY", "mode": "encrypt"}, {"result": "RIJVS"}),
    ]
)
def test_vigenere_cipher_with_allowany_permission(rf, api_endpoints, data, expected_result):
    url = api_endpoints["vigenere_cipher"]
    with allure.step(f"Send unauthenticated POST request to {url}"):
        request = rf.post(url, data=data)
        response = vigenere_cipher_view(request)

    with allure.step("Assert status code is 200 OK and valid response returned"):
        assert response.status_code == status.HTTP_200_OK
        assert response["Content-Type"] == "text/html; charset=utf-8"
        response.render()
        json_data = json.loads(response.content.decode("utf-8"))
        assert json_data == expected_result
