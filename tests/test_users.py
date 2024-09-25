from allure_commons._allure import step
from faker import Faker

from reqres_tests.utils.logger import send_reqres
from reqres_tests.utils.schema import validate_schema

fake = Faker()


def test_create_user():
    name = fake.name()
    job = fake.job()
    data = {"name": name, "job": job}

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


def test_update_user_put():
    name = fake.name()
    job = fake.job()
    data = {"name": name, "job": job}
    with step('Обновить пользователя'):
        response = send_reqres('/api/users/2', 'put', json=data)

    with step('Статус код == 200'):
        assert response.status_code == 200

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body["name"] == name
        assert body["job"] == job

    with step('Валидировать схему'):
        validate_schema(body, "update_user.json")


def test_update_user_patch():
    name = fake.name()
    job = fake.job()
    data = {"name": name, "job": job}
    with step('Обновить пользователя'):
        response = send_reqres('/api/users/2', 'patch', json=data)

    with step('Статус код == 200'):
        assert response.status_code == 200

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body["name"] == name
        assert body["job"] == job

    with step('Валидировать схему'):
        validate_schema(body, "update_user.json")


def test_delete_user():
    with step('Удалить пользователя'):
        response = send_reqres('/api/users/2', 'delete')

    with step('Статус код == 204'):
        assert response.status_code == 204

    with step('Проверить, что ответ пустой'):
        assert response.text == ''


def test_delayed_response():
    with step('Удалить пользователя'):
        response = send_reqres('/api/users?delay=3', 'get')

    with step('Статус код == 200'):
        assert response.status_code == 200
