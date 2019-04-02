# coding=utf-8
import unittest


class TestCase_01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('这是所有case的前置条件01')

    @classmethod
    def tearDownClass(cls):
        print('这是所有case的后置条件01')

    def setUp(self):
        print('这是每条case的前置条件01')

    def tearDown(self):
        print('这是每条case的后置条件01')

    def testThird_01(self):
        print('01: 第三条case')

    def testFirst_01(self):
        print('01: 第一条case')

    @unittest.skip('不执行这条case')
    def testSecond_01(self):
        print('01: 第二条case')

    def testFourth_01(self):
        print('01: 第四条case')
