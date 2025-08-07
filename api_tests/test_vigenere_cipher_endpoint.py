import json
import pytest

from rest_framework import status
from django.core.exceptions import RequestDataTooBig

from backend.views import vigenere_cipher_view


@pytest.mark.parametrize(
    "payload, expected_status, expected_response",
    [
        ({"text": "HELLO", "key": "KEY", "mode": "encrypt"}, status.HTTP_200_OK, {"result": "RIJVS"}),
        ({"text": "RIJVS", "key": "KEY", "mode": "decrypt"}, status.HTTP_200_OK, {"result": "HELLO"}),
        ({"text": "HELLO", "mode": "encrypt"}, status.HTTP_400_BAD_REQUEST, {"error": "Key is required."}),
        ({"text": "HELLO", "key": "", "mode": "encrypt"}, status.HTTP_400_BAD_REQUEST, {"error": "Key is required."}),
        ({"text": "HELLO", "key": "KEY", "mode": "invalid_mode"}, status.HTTP_200_OK, None),
        # result presence checked separately
    ],
)
def test_vigenere_cipher_post_requests(rf, vigenere_cipher_url, payload, expected_status, expected_response):
    request = rf.post(vigenere_cipher_url, data=payload)
    response = vigenere_cipher_view(request)

    assert response.status_code == expected_status
    assert response["Content-Type"] == "text/html; charset=utf-8"
    response.render()
    json_data = json.loads(response.content.decode("utf-8"))

    if expected_response is not None:
        assert json_data == expected_response
    else:
        # For invalid mode test, just verify that 'result' key exists
        assert "result" in json_data


def test_vigenere_cipher_view_text_size_limit(rf, vigenere_cipher_url):
    large_text = "A" * (10 * 1024 * 1024 + 1)  # 10 MB + 1 byte
    with pytest.raises(RequestDataTooBig):
        request = rf.post(vigenere_cipher_url, data={"text": large_text, "key": "KEY", "mode": "encrypt"})
        vigenere_cipher_view(request)


@pytest.mark.parametrize(
    "method",
    ["get", "put", "delete", "patch"]
)
def test_vigenere_cipher_view_disallowed_methods(rf, vigenere_cipher_url, method):
    request_method = getattr(rf, method)
    request = request_method(vigenere_cipher_url)
    response = vigenere_cipher_view(request)

    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert response["Content-Type"] == "text/html; charset=utf-8"
    response.render()
    json_data = json.loads(response.content.decode("utf-8"))
    assert json_data == {'detail': f'Method "{method.upper()}" not allowed.'}


@pytest.mark.parametrize(
    "data, expected_result",
    [
        ({"text": "HELLO", "key": "KEY", "mode": "encrypt"}, {"result": "RIJVS"}),
    ]
)
def test_vigenere_cipher_with_allowany_permission(rf, vigenere_cipher_url, data, expected_result):
    request = rf.post(vigenere_cipher_url, data=data)
    response = vigenere_cipher_view(request)

    assert response.status_code == status.HTTP_200_OK
    assert response["Content-Type"] == "text/html; charset=utf-8"
    response.render()
    json_data = json.loads(response.content.decode("utf-8"))
    assert json_data == expected_result
