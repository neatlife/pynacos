# coding=utf-8
import unittest

from pynacos import nacosconfig


class TestCaseNacosConfig(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        nacosconfig.host = 'http://127.0.0.1:8848'

    def test_get(self):
        assert nacosconfig.name == 'nacos-client'

    def test_get_env(self):
        assert nacosconfig.env == 'dev'

    def test_get_host(self):
        assert nacosconfig.host == 'http://127.0.0.1:8848';
