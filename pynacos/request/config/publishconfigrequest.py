# coding=utf-8
from pynacos.request.config.configrequest import ConfigRequest


class PublishConfigRequest(ConfigRequest):
    uri = "/nacos/v1/cs/configs"

    verb = "POST"

    # 配置内容
    content = None
