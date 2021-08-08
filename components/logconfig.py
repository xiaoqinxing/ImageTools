import logging

import datetime   # 时间模块
import os

# 设置日志存放路径
path = '.\\log\\'
if(not os.path.exists(path)):
    os.mkdir(path)

# 获取今天的日期 格式2019-08-01
today_date = str(datetime.date.today())


def init_log():
    logging.basicConfig(
        filename=path + today_date + '.log',
        level=logging.DEBUG, filemode='a',
        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M',
        encoding='utf-8'
    )
    logging.info('logging module init is ok')


def clean_old_log():
    """
    删除今天以外的日志
    """
    global path
    global today_date

    # 遍历目录下的所有日志文件 i是文件名
    for i in os.listdir(path):
        if(i != today_date + '.log'):
            os.remove(path + i)
