from allure_commons._allure import step

from reqres_tests.data import register_user_data
from reqres_tests.utils.logger import send_reqres
from reqres_tests.utils.schema import validate_schema


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
