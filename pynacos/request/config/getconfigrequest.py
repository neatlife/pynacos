# coding=utf-8
from pynacos.request.config.configrequest import ConfigRequest


class GetConfigRequest(ConfigRequest):
    uri = "/nacos/v1/cs/configs"

    verb = "GET"
