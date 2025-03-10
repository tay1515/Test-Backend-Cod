from _pydatetime import datetime

import pytest
from typing import Generator
from playwright.sync_api import Playwright, APIRequestContext


@pytest.fixture(scope="session")
def user_ids():
    ids = []
    yield ids


@pytest.fixture(scope="session")
def user_api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="https://reqres.in"
    )
    yield request_context
    request_context.dispose()


def test_exit_case_1(user_api_request_context: APIRequestContext, user_ids) -> None:
    payload = {
        "name": "Tyrone",
        "job": "QA testing",
    }

    response = user_api_request_context.post(url="/api/users", data=payload)
    assert response.ok
    assert response.status == 201

    json_response = response.json()
    print("API Response:\n{}".format(json_response))
    print("Name: " + json_response["name"])
    assert json_response["name"] == payload.get("name")
    assert json_response["job"] == payload.get("job")
    user_ids.append(json_response["id"])

def test_exit_case_2(user_api_request_context: APIRequestContext, user_ids) -> None:
    payload = {
        "name": "Maria Zapata",
        "job": "Analist",
        "gender": "Female",
        "age": 33
    }

    response = user_api_request_context.post(url="/api/users", data=payload)
    assert response.ok
    assert response.status == 201

    json_response = response.json()
    print("API Response:\n{}".format(json_response))
    print("Name: " + json_response["name"])
    assert json_response["name"] == payload.get("name")
    assert json_response["job"] == payload.get("job")
    assert json_response["gender"] == payload.get("gender")
    assert json_response["age"] == payload.get("age")
    assert type(json_response["age"]) == int
    assert type(json_response["createdAt"]) != ""
    user_ids.append(json_response["id"])

def test_exit_case_3(user_api_request_context: APIRequestContext, user_ids) -> None:
    payload = {
        "name": "Maria Zapata",
        "job": "Analist",
    }

    response = user_api_request_context.post(url="/[api/users", data=payload)
    assert response.status == 404

