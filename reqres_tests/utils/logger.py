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
    return response


def log(response):
    curl = curlify.to_curl(response.request)
    logging.info(curl)
    allure.attach(body=curl, name='curl', attachment_type=AttachmentType.TEXT, extension='txt')


# def get_reqres(url, **kwargs):
#     with step(f'GET {url}'):
#         response = requests.get(BASE_URL + url, **kwargs)
#         curl = curlify.to_curl(response.request)
#         logging.info(curl)
#         allure.attach(body=curl, name='curl', attachment_type=AttachmentType.TEXT, extension='txt')
#     return response
#
#
# def post_reqres(url, **kwargs):
#     with step(f'POST {url}'):
#         response = requests.post(BASE_URL + url, **kwargs)
#         curl = curlify.to_curl(response.request)
#         logging.info(curl)
#         allure.attach(body=curl, name='curl', attachment_type=AttachmentType.TEXT, extension='txt')
#     return response
#
#
# def delete_reqres(url, **kwargs):
#     with step(f'DELETE {url}'):
#         response = requests.delete(BASE_URL + url, **kwargs)
#         curl = curlify.to_curl(response.request)
#         logging.info(curl)
#         allure.attach(body=curl, name='curl', attachment_type=AttachmentType.TEXT, extension='txt')
#     return response
