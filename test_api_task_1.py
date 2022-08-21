import re
import pytest
import requests

url = 'https://reqres.in/api/users'


def test_get_users():
    params = {'page': 2}
    pattern = "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$"

    response = requests.get(url=url, params=params)
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

    response_body = response.json()
    assert "page" in response_body
    assert isinstance(response_body["page"], int)
    assert "per_page" in response_body
    assert isinstance(response_body["per_page"], int)
    assert "total" in response_body
    assert isinstance(response_body["total"], int)
    assert "total_pages" in response_body
    assert isinstance(response_body["total_pages"], int)
    assert "data" in response_body
    assert isinstance(response_body["data"], list)

    users_data = response_body['data']
    for user_data in users_data:
        assert "id" in user_data
        assert isinstance(user_data["id"], int)
        assert "email" in user_data
        assert isinstance(user_data["email"], str)
        assert re.match(pattern, user_data["email"])
        assert "first_name" in user_data
        assert isinstance(user_data["first_name"], str)
        assert "last_name" in user_data
        assert isinstance(user_data["last_name"], str)
        assert "avatar" in user_data
        assert isinstance(user_data["avatar"], str)

    assert "support" in response_body
    assert isinstance(response_body["support"], dict)
    assert "url" in response_body['support']
    assert isinstance(response_body["support"]["url"], str)
    assert "text" in response_body['support']
    assert isinstance(response_body["support"]["text"], str)


def test_create_user():
    body = {"name": "morpheus", "job": "leader"}
    response = requests.post(url=url, json=body)
    assert response.status_code == 201
    assert "application/json" in response.headers["Content-Type"]

    response_body = response.json()
    for key in body:
        assert key in response_body
        assert response_body[key] == body[key]
