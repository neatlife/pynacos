# coding=utf-8
from pynacos import nacosconfig
from pynacos.request.config.configrequest import ConfigRequest
from pynacos.util import encode


class ListenerConfigRequest(ConfigRequest):
    uri = "/nacos/v1/cs/configs/listener"

    verb = "POST"

    # 监听数据报文。格式为 dataId^2Group^2contentMD5^2tenant^1或者dataId^2Group^2contentMD5^1。
    LISTENING_CONFIGS_FORMAT = "%s%s%s%s%s%s%s%s"

    # 监听数据报文
    listeningConfigs = None

    # 配置内容 MD5 值
    contentMD5 = None

    # 长轮询等待时间
    longPullingTimeout = None

    def get_long_puling_timeout(self):
        if self.longPullingTimeout is None:
            return nacosconfig.longPullingTimeout
        else:
            return self.longPullingTimeout

    def get_listener_confgs(self):
        return self.LISTENING_CONFIGS_FORMAT % (
            self.dataId,
            encode.two_encode,
            self.group,
            encode.two_encode,
            self.contentMD5,
            encode.two_encode,
            self.tenant,
            encode.one_encode
        )
