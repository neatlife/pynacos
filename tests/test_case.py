# coding=utf-8
import unittest

from pynacos import nacosconfig


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        nacosconfig.group = 'DEFAULT_GROUP'
        nacosconfig.tenant = ''
        nacosconfig.dataId = 'LARAVEL'
        nacosconfig.host = 'http://127.0.0.1:8848'
