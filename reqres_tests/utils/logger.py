import logging

import allure
import curlify
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType

BASE_URL = 'https://reqres.in'


def get_reqres(url, **kwargs):
    with step(f'POST {url}'):
        response = requests.get(BASE_URL + url, **kwargs)
        curl = curlify.to_curl(response.request)
        logging.info(curl)
        allure.attach(body=curl, name='curl', attachment_type=AttachmentType.TEXT, extension='txt')
    return response


def post_reqres(url, **kwargs):
    with step(f'POST {url}'):
        response = requests.post(BASE_URL + url, **kwargs)
        curl = curlify.to_curl(response.request)
        logging.info(curl)
        allure.attach(body=curl, name='curl', attachment_type=AttachmentType.TEXT, extension='txt')
    return response


def delete_reqres(url, **kwargs):
    with step(f'POST {url}'):
        response = requests.delete(BASE_URL + url, **kwargs)
        curl = curlify.to_curl(response.request)
        logging.info(curl)
        allure.attach(body=curl, name='curl', attachment_type=AttachmentType.TEXT, extension='txt')
    return response
