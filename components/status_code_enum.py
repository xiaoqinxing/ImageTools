from enum import Enum
from logging import error
from traceback import format_exc
from components.customwidget import critical_win


class StatusCode(Enum):
    """状态码枚举类"""
    OK = '成功'
    ERROR = '错误'
    FILE_NOT_FOUND = '文件不存在'
    FILE_PATH_NOT_VALID = '文件路径不合法'
    IMAGE_FORMAT_ERR = '图像格式错误'
    IMAGE_FORMAT_NOT_SUPPORT = '图像格式不支持'
    IMAGE_READ_ERR = '图像读取失败'
    IMAGE_IS_NONE = '图片为空'


class ImageToolError(Exception):
    def show(self):
        error(format_exc())
        critical_win(str(self))


class FileNotFoundErr(ImageToolError):
    def __init__(self):
        super().__init__('文件不存在')


class FilePathNotValidErr(ImageToolError):
    def __init__(self):
        super().__init__('文件路径不合法')


class ImageFormatErr(ImageToolError):
    def __init__(self):
        super().__init__('图像格式错误')


class ImageFormatNotSupportErr(ImageToolError):
    def __init__(self):
        super().__init__('图像格式不支持')


class ImageReadErr(ImageToolError):
    def __init__(self):
        super().__init__('图像读取失败')


class ImageNoneErr(ImageToolError):
    def __init__(self):
        super().__init__('图片为空')
