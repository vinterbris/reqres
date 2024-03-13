from allure_commons._allure import step

from reqres_tests.data import create_user_name, create_user_job, create_user_data
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
