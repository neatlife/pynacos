import requests

from pynacos import nacosconfig
from pynacos.const import verbconst


def get(uri, body=None, headers=None):
    return request(verbconst.GET, uri, body, headers)


def post(uri, body=None, headers=None):
    return request(verbconst.POST, uri, body, headers)


def request(verb, uri, body=None, headers=None):
    if headers is None:
        headers = {}
    if body is None:
        body = {}

    url = nacosconfig.host + uri
    if str.upper(verb) == verbconst.GET:
        response = requests.get(url, body, headers=headers)
    else:
        response = requests.request(verb, url, data=body, headers=headers)

    return response
