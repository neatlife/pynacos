# coding=utf-8

from pynacos import nacosconfig
from pynacos.request.request import Request
from pynacos.util import case
from pynacos.util import log
from pynacos.util import reflection


class ConfigRequest(Request):
    # 租户信息，对应 Nacos 的命名空间字段。
    tenant = None

    # 配置 ID
    dataId = None

    # 配置分组。
    group = None

    def get_parameter_and_header(self):
        parameter_list = {}
        header_list = {}
        for property, value in reflection.getProperties(self).items():
            if property in self.standaloneParameterList:
                pass
            elif property == 'longPullingTimeout':
                header_list['Long-Pulling-Timeout'] = str(getattr(self, 'get_long_puling_timeout')())
            elif property == 'listeningConfigs':
                parameter_list['Listening-Configs'] = getattr(self, 'get_listener_confgs')()
            else:
                parameter_list[case.camel_case(property)] = value
        if nacosconfig.isDebug:
            log.info("parameter_list: %s, header_list: %s" % (parameter_list, header_list))
            pass
        return [parameter_list, header_list]
