from allure_commons._allure import step

from reqres_tests.data import single_user_data, create_user_data, create_user_name, create_user_job, register_user_data, \
    users_list, login_data
from reqres_tests.utils.logger import get_reqres, post_reqres, delete_reqres
from reqres_tests.utils.schema import validate_schema


def test_get_single_user():
    data = single_user_data

    with step('Получить информацию о единственном пользователе'):
        response = get_reqres('/api/users/2')

    with step('Статус код == 200'):
        assert response.status_code == 200

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body['data'] == data

    with step('Валидировать схему'):
        validate_schema(body, "single_user.json")


def test_create_user():
    name = create_user_name
    job = create_user_job
    data = create_user_data

    with step('Создать пользователя'):
        response = post_reqres('/api/users/', json=data)

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
        response = post_reqres('/api/register', json=data)

    with step('Статус код == 200'):
        assert response.status_code == 200

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body['id'] == 4
        assert body['token'] == 'QpwL5tke4Pnpja7X4'

    with step('Валидировать схему'):
        validate_schema(body, "registration.json")


def test_list_users():
    data = users_list

    with step('Получить список пользователей'):
        response = get_reqres('/api/users?page=2')

    with step('Статус код == 200'):
        assert response.status_code == 200

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body['page'] == 2
        assert body['data'] == data

    with step('Валидировать схему'):
        validate_schema(body, "get_users_list.json")


def test_login_successful():
    data = login_data

    with step('Произвести логин'):
        response = post_reqres('/api/login', json=data)

    with step('Статус код == 200'):
        assert response.status_code == 200

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body['token'] == 'QpwL5tke4Pnpja7X4'

    with step('Валидировать схему'):
        validate_schema(body, "login_successful.json")


def test_delete_user_status_code():
    response = delete_reqres('/api/users/2')

    with step('Статус код == 200'):
        assert response.status_code == 204

    with step('Проверить, что ответ пустой'):
        assert response.text == ''
