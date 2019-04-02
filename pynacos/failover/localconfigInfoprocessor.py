# coding=utf-8

import os

from pynacos import nacosconfig
from pynacos.failover.processor import Processor
from pynacos.util import file


class LocalConfigInfoProcessor(Processor):
    @staticmethod
    def get_failover(server_name, data_id, group, tenant):
        failoverFile = LocalConfigInfoProcessor.get_failover_file(server_name, data_id, group, tenant)
        if not os.path.isfile(failoverFile):
            return None
        return file.read(failoverFile)

    @staticmethod
    def get_failover_file(server_name, data_id, group, tenant):
        failover_file = nacosconfig.snapshotPath + os.sep + server_name + '_nacos' + os.sep
        if tenant:
            failover_file = failover_file + "config-data-tenant" + os.sep + tenant + os.sep
        else:
            failover_file = failover_file + "config-data" + os.sep
        return failover_file

    # 获取本地缓存文件内容。NULL表示没有本地文件或抛出异常。
    @staticmethod
    def get_snapshot(name, data_id, group, tenant):
        snapshot_file = LocalConfigInfoProcessor.get_snapshot_file(name, data_id, group, tenant)
        if not os.path.isfile(snapshot_file):
            return None
        return file.read(snapshot_file)

    @staticmethod
    def get_snapshot_file(env_name, data_id, group, tenant):
        snapshot_file = nacosconfig.snapshotPath + os.sep + env_name + '_nacos' + os.sep
        if tenant:
            snapshot_file += "snapshot-tenant" + os.sep + tenant + os.sep
        else:
            snapshot_file += "snapshot" + os.sep
        return snapshot_file + data_id

    @staticmethod
    def save_snapshot(env_name, data_id, group, tenant, config):
        snapshot_file = LocalConfigInfoProcessor.get_snapshot_file(env_name, data_id, group, tenant)
        if not config:
            file.delete(snapshot_file)
        else:
            if not os.path.exists(os.path.dirname(snapshot_file)):
                file.mkdir_p(os.path.dirname(snapshot_file))
            file.write(snapshot_file, config)
