from allure_commons._allure import step

from reqres_tests.data import single_resource_data, resources_list
from reqres_tests.utils.logger import send_reqres
from reqres_tests.utils.schema import validate_schema


def test_get_single_resource():
    data = single_resource_data

    with step('Получить информацию о единственном пользователе'):
        response = send_reqres('/api/unknown/2', 'get')

    with step('Статус код == 200'):
        assert response.status_code == 200

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body['data'] == data

    with step('Валидировать схему'):
        validate_schema(body, "single_resource.json")


def test_list_resources():
    data = resources_list

    with step('Получить список пользователей'):
        response = send_reqres('/api/unknown', 'get')

    with step('Статус код == 200'):
        assert response.status_code == 200

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body['page'] == 1
        assert body['data'] == data

    with step('Валидировать схему'):
        validate_schema(body, "list_resources.json")


def test_resource_not_found():
    with step('Получить информацию о ресурсе'):
        response = send_reqres('/api/unknown/23', 'get')

    with step('Статус код == 404'):
        assert response.status_code == 404

    with step('Проверить корректность ответа'):
        body = response.json()
        assert body == {}
