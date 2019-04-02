# coding=utf-8
import unittest
import os

from pynacos import nacosconfig
from pynacos.nacos import Nacos
from pynacos.failover.localconfigInfoprocessor import LocalConfigInfoProcessor


class TestCaseNacos(unittest.TestCase):

    def test_run_once(self):
        Nacos.init(
            'http://127.0.0.1:8848',
            'dev',
            'LARAVEL',
            'DEFAULT_GROUP',
            ''
        ).run_once()
        snapshot_file = LocalConfigInfoProcessor.get_snapshot_file(
            'dev',
            'LARAVEL',
            'DEFAULT_GROUP',
            ''
        )
        self.assertTrue(os.path.isfile(snapshot_file))

    def test_listener(self):
        nacosconfig.longPullingTimeout = 10000
        Nacos.init(
            'http://127.0.0.1:8848',
            'dev',
            'LARAVEL',
            'DEFAULT_GROUP',
            ''
        ).listener()

