# coding=utf-8
import os

from pynacos.request.config.getconfigrequest import GetConfigRequest
from tests.test_case import TestCase


class TestCaseHttp(TestCase):

    def test_get_config_request(self):
        get_config_request = GetConfigRequest()
        get_config_request.group = 'DEFAULT_GROUP'
        get_config_request.dataId = 'LARAVEL'
        get_config_request.tenant = ''
        response = get_config_request.do_request()
        print "content: " + os.linesep + response.content
        self.assertIsNotNone(response.content)
