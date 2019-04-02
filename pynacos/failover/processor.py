# coding=utf-8

import os

from pynacos import nacosconfig
from pynacos.util import file


class Processor():
    def __init__(self):
        pass

    # 清除snapshot目录下所有缓存文件。
    @staticmethod
    def clean_all_snapshot():
        file.delete_all(nacosconfig.snapshotPath)

    @staticmethod
    def cleanEnvSnapshot(env_name):
        envSnapshotPath = nacosconfig.snapshotPath + os.sep + env_name + "_nacos" + os.sep;
        file.delete_all(envSnapshotPath)
