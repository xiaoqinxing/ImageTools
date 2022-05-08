from enum import Enum


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
