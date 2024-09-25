from allure_commons._allure import step
from faker import Faker

from reqres_tests.data import (
    login_data,
    login_data_incomplete,
)
from reqres_tests.utils.logger import send_reqres
from reqres_tests.utils.schema import validate_schema

fake = Faker()


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


class TestRegistration:
    def test_register_user_successful(self):
        password = fake.password()
        data = {"email": "eve.holt@reqres.in", "password": password}

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

    def test_register_user_without_password(self):
        email = fake.email()
        data = {"email": email}

        with step('Зарегистрировать пользователя'):
            response = send_reqres('/api/register', 'post', json=data)

        with step('Статус код == 400'):
            assert response.status_code == 400

        with step('Проверить корректность ответа'):
            body = response.json()
            assert body['error'] == "Missing password"

        with step('Валидировать схему'):
            validate_schema(body, "regsiter_user_unsuccessful.json")

    def test_register_user_without_login(self):
        password = fake.password()
        data = {"password": password}

        with step('Зарегистрировать пользователя'):
            response = send_reqres('/api/register', 'post', json=data)

        with step('Статус код == 400'):
            assert response.status_code == 400

        with step('Проверить корректность ответа'):
            body = response.json()
            assert body['error'] == "Missing email or username"

    def test_register_user_without_body(self):
        data = {}

        with step('Зарегистрировать пользователя'):
            response = send_reqres('/api/register', 'post', json=data)

        with step('Статус код == 400'):
            assert response.status_code == 400

        with step('Проверить корректность ответа'):
            body = response.json()
            assert body['error'] == "Missing email or username"