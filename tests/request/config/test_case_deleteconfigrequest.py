# coding=utf-8
import os

from pynacos.request.config.deleteconfigrequest import DeleteConfigRequest
from tests.test_case import TestCase
from pynacos.util import file


class TestCaseHttp(TestCase):

    def test_delete_config_request(self):
        delete_config_request = DeleteConfigRequest()
        delete_config_request.group = 'DEFAULT_GROUP'
        delete_config_request.dataId = 'LARAVEL2'
        delete_config_request.tenant = ''

        response = delete_config_request.do_request()
        print "content: " + os.linesep + response.content
        self.assertIsNotNone(response.content)
