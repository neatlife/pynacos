# coding=utf-8
import os

from pynacos.request.config.listenerconfigrequest import ListenerConfigRequest
from tests.test_case import TestCase


class TestCaseHttp(TestCase):

    def test_listener_config_request(self):
        listener_config_request = ListenerConfigRequest()
        listener_config_request.group = 'DEFAULT_GROUP'
        listener_config_request.dataId = 'LARAVEL'
        listener_config_request.tenant = ''
        listener_config_request.contentMD5 = 'ddf41f9b16c588e0f6a185f4c82bf61d'
        response = listener_config_request.do_request()
        print "content: " + os.linesep + response.content
        self.assertIsNotNone(response.content)
