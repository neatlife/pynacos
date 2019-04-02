# coding=utf-8
import sys

from pynacos.error.configerror import ConfigNotFoundError


class NacosConfig:
    name = 'nacos-client'
    env = 'dev'
    host = None
    tenant = None
    dataId = None
    group = None
    snapshotPath = 'nacos/config'
    longPullingTimeout = 30000
    isDebug = False

    def __setattr__(self, name, value):
        if hasattr(self, name) is False:
            raise ConfigNotFoundError("不存在这个配置设置项 %s" % name)
        self.__dict__[name] = value

    def __getattr__(self, name):
        if hasattr(self, name) is False:
            raise ConfigNotFoundError("不存在这个配置读取项 %s" % name)
        return self.__dict__[name]


sys.modules[__name__] = NacosConfig()
