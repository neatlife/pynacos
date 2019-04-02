# coding=utf-8

import hashlib


def md5(content):
    m = hashlib.md5()
    m.update(content)
    return m.hexdigest()
