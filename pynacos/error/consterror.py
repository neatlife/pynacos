# coding=utf-8


# 修改配置项异常
class ConstError(RuntimeError):
    pass


# 配置项格式异常
class ConstCaseError(ConstError):
    pass
