from allure_commons._allure import step

from reqres_tests.data import (
    login_data,
    register_user_data,
    register_user_data_incomplete,
    login_data_incomplete,
)
from reqres_tests.utils.logger import send_reqres
from reqres_tests.utils.schema import validate_schema


def test_login_successful():
    data = login_data

    with step('Произвести логин'):
        response = send_reqres('/api/login', 'post', json=data)

    with step('Статус код == 200'):
        assert response.status_code == 200

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body['token'] == 'QpwL5tke4Pnpja7X4'

    with step('Валидировать схему'):
        validate_schema(body, "login_successful.json")


def test_login_unsuccessful():
    data = login_data_incomplete

    with step('Произвести логин'):
        response = send_reqres('/api/login', 'post', json=data)

    with step('Статус код == 400'):
        assert response.status_code == 400

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body['error'] == "Missing password"

    with step('Валидировать схему'):
        validate_schema(body, "login_user_unsuccessful.json")


def test_register_user_successful():
    data = register_user_data

    with step('Зарегистрировать пользователя'):
        response = send_reqres('/api/register', 'post', json=data)

    with step('Статус код == 200'):
        assert response.status_code == 200

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body['id'] == 4
        assert body['token'] == 'QpwL5tke4Pnpja7X4'

    with step('Валидировать схему'):
        validate_schema(body, "registration.json")


def test_register_user_unsuccessful():
    data = register_user_data_incomplete

    with step('Зарегистрировать пользователя'):
        response = send_reqres('/api/register', 'post', json=data)

    with step('Статус код == 400'):
        assert response.status_code == 400

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body['error'] == "Missing password"

    with step('Валидировать схему'):
        validate_schema(body, "regsiter_user_unsuccessful.json")
