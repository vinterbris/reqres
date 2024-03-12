from allure_commons._allure import step

from reqres_tests.data import create_user_name, create_user_job, create_user_data, register_user_data, login_data
from reqres_tests.utils.logger import send_reqres
from reqres_tests.utils.schema import validate_schema


def test_create_user():
    name = create_user_name
    job = create_user_job
    data = create_user_data

    with step('Создать пользователя'):
        response = send_reqres('/api/users/', 'post', json=data)

    with step('Статус код == 201'):
        assert response.status_code == 201

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body["name"] == name
        assert body["job"] == job

    with step('Валидировать схему'):
        validate_schema(body, "create_user.json")


def test_register_user():
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
