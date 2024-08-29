<h1 align="center">Проект API тестов <a href="https://reqres.in">reqres.in</a></h1>

<h3 align="center">Python | Pytest | Requests | Jenkins | Allure | Telegram</h3>
<h3 align="center">
<img height="50" src="resources/images/Python.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/Pytest.svg"/>      &nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/requests.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/jenkins.png"/>     &nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/allure.png"/>      &nbsp;&nbsp;&nbsp;&nbsp;
<img height="50" src="resources/images/telegram.png"/>
</h3>

---

### Реализованы тесты:
#### API
- [x] Создание пользователя
- [x] Обновление пользователя
- [x] Удаление пользователя

- [x] Получение списка пользователей
- [x] Получение информации об одном пользователе
- [x] Пользователь не найден

- [x] Получение информации о ресурсе
- [x] Получение информации о списке ресурсов
- [x] Ресурс не найден

- [x] Успешная регистрация пользователя
- [x] Неуспешная регистрация пользователя
- [x] Успешный логин пользователя
- [x] Неуспешный логин пользователя
- [x] Ответ с задержкой

> <a target="_blank" href="http://176.123.163.26:8888/job/Reqres-project/">Ссылка на проект в мой Jenkins: доступны прогоны и allure отчёты</a>


## Запуск тестов

### Локально

1. Клонировать репозиторий 
```bash
git clone https://github.com/vinterbris/qa_guru_python_9_24.git
```
2. В терминале в директории проекта создать и активировать виртуальное окружение
```bash
python -m venv .venv 
source .venv/bin/activate 
```
3. Установить зависимости
```
pip install -r requirements.txt 
```
4. Запустить командой
```bash
pytest
```

#### Получение отчета allure
```bash
allure serve
```

## Оповещения в мессенджер

> _Настроена отправка оповещений в телеграм канал. Возможна настройка для Email,Slack, Discord, Skype, Mattermost, Rocket.Chat_

<img src="resources/images/screenshot_telegram.png" width="450" height="">