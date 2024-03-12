from allure_commons._allure import step

from reqres_tests.utils.logger import send_reqres


def test_delete_user():
    response = send_reqres('/api/users/2', 'delete')

    with step('Статус код == 200'):
        assert response.status_code == 204

    with step('Проверить, что ответ пустой'):
        assert response.text == ''
