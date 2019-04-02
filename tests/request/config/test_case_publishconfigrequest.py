# coding=utf-8
import os

from pynacos.request.config.publishconfigrequest import PublishConfigRequest
from tests.test_case import TestCase
from pynacos.util import file


class TestCaseHttp(TestCase):

    def test_publish_config_request(self):
        publish_config_request = PublishConfigRequest()
        publish_config_request.group = 'DEFAULT_GROUP'
        publish_config_request.dataId = 'LARAVEL2'
        publish_config_request.tenant = ''
        publish_config_request.content = file.read("env-example")

        response = publish_config_request.do_request()
        print "content: " + os.linesep + response.content
        self.assertIsNotNone(response.content)
