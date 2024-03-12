from allure_commons._allure import step

from reqres_tests.data import single_user_data, users_list
from reqres_tests.utils.logger import send_reqres
from reqres_tests.utils.schema import validate_schema


def test_get_single_user():
    data = single_user_data

    with step('Получить информацию о единственном пользователе'):
        response = send_reqres('/api/users/2', 'get')

    with step('Статус код == 200'):
        assert response.status_code == 200

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body['data'] == data

    with step('Валидировать схему'):
        validate_schema(body, "single_user.json")


def test_list_users():
    data = users_list

    with step('Получить список пользователей'):
        response = send_reqres('/api/users?page=2', 'get')

    with step('Статус код == 200'):
        assert response.status_code == 200

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body['page'] == 2
        assert body['data'] == data

    with step('Валидировать схему'):
        validate_schema(body, "get_users_list.json")
