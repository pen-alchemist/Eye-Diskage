import pytest

from django.test import Client


@pytest.fixture
def client_django():
    return Client()
