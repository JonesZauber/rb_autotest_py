import pytest
import requests


def test_status_code():
    response = requests.get('https://www.redbull.com/')
    assert response.status_code == 200





