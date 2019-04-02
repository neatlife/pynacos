# coding=utf-8

from pynacos import nacosconfig
from pynacos.nacosclient import NacosClient


class Nacos():
    __instance = None

    @staticmethod
    def init(host, env, data_id, group, tenant):
        if Nacos.__instance is None:
            nacosconfig.host = host
            nacosconfig.env = env
            nacosconfig.dataId = data_id
            nacosconfig.group = group
            nacosconfig.tenant = tenant
            Nacos.__instance = Nacos()
        return Nacos.__instance

    @staticmethod
    def run_once():
        return NacosClient.get(nacosconfig.env, nacosconfig.dataId, nacosconfig.group, nacosconfig.tenant)

    @staticmethod
    def listener():
        NacosClient.listener(nacosconfig.env, nacosconfig.dataId, nacosconfig.group, nacosconfig.tenant)
