# coding=utf-8
from pynacos.request.config.configrequest import ConfigRequest


class DeleteConfigRequest(ConfigRequest):
    uri = "/nacos/v1/cs/configs"

    verb = "DELETE"
