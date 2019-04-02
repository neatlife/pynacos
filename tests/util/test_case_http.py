# coding=utf-8
import os

from pynacos.util import http
from tests.test_case import TestCase


class TestCaseHttp(TestCase):

    def test_get(self):
        response = http.get("/nacos/v1/cs/configs", {"dataId": "LARAVEL", "group": "DEFAULT_GROUP"})
        print("content: " + os.linesep + response.content)
        self.assertIsNotNone(response.content)
