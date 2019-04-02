# coding=utf-8

from pynacos.error.request import ParameterRequiredError
from pynacos.error.response import ResponseCodeError
from pynacos.util import http


class Request:

    # 接口地址
    def __init__(self):
        pass

    uri = None

    # 接口动词
    verb = None

    # 忽略这些属性
    standaloneParameterList = ['uri', 'verb', 'standaloneParameterList']

    # 获取请求参数和请求头
    def get_parameter_and_header(self):
        raise NotImplementedError("Must override get_parameter_and_header")

    # 发起请求，做返回值异常检查
    def do_request(self):
        self.require_not_null()
        parameter_list, header_list = self.get_parameter_and_header()
        response = http.request(self.verb, self.uri, parameter_list, header_list)
        self.handle_error_code(response.status_code)
        return response

    @staticmethod
    def handle_error_code(statusCode):
        error_code_map = {
            400: '客户端请求中的语法错误',
            401: '未授权',
            403: '没有权限',
            404: '无法找到资源',
            500: '服务器内部错误',
        }
        if error_code_map.get(statusCode) is not None:
            raise ResponseCodeError(error_code_map.get(statusCode))

    def require_not_null(self):
        if self.uri is None:
            raise ParameterRequiredError("uri 参数不能为空")
        if self.verb is None:
            raise ParameterRequiredError("verb 参数不能为空")
