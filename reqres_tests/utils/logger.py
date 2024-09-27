import json
import logging

import allure
import curlify
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType

from tests.conftest import BASE_URL


def send_reqres(url, method, **kwargs):
    if method == 'get':
        with step(f'GET {url}'):
            response = requests.get(BASE_URL + url, **kwargs)
            log(response)
    elif method == 'post':
        with step(f'POST {url}'):
            response = requests.post(BASE_URL + url, **kwargs)
            log(response)
    elif method == 'delete':
        with step(f'DELETE {url}'):
            response = requests.delete(BASE_URL + url, **kwargs)
            log(response)
    elif method == 'put':
        with step(f'PUT {url}'):
            response = requests.put(BASE_URL + url, **kwargs)
            log(response)
    elif method == 'patch':
        with step(f'PATCH {url}'):
            response = requests.patch(BASE_URL + url, **kwargs)
            log(response)
    elif method == 'options':
        with step(f'OPTIONS {url}'):
            response = requests.options(BASE_URL + url, **kwargs)
            log(response)
    return response


def log(response):
    curl = curlify.to_curl(response.request)
    logging.info(curl)
    allure.attach(body=curl, name='curl', attachment_type=AttachmentType.TEXT, extension='txt')
    allure.attach(body=response.request.method + " " + response.request.url, name="Request",
                  attachment_type=AttachmentType.TEXT, extension="txt")
    if response.text:
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
