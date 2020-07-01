#自定义的异常处理方式

from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler

def exception_handler(exc, context):
    # 详细错误信息的定义
    error = "%s %s %s" % (context['view'], context['request'].method, exc)
    print(error)

    # 先让DRF处理异常 根据异常的返回值可以判断异常是否被处理
    response = drf_exception_handler(exc, context)
    # 如果返回值为None，代表DRF无法处理此时发生的异常  需要自定义处理
    if response is None:
        return Response({"error_msg": "给老子等一会"})

    # 如果Response不为空  说明异常信息已经被DRF处理了 直接返回即可
    return response