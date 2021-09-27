import datetime
import os
import logging

# 设置日志存放路径
LOGFILE_PATH = '.\\log\\'
if not os.path.exists(LOGFILE_PATH):
    os.mkdir(LOGFILE_PATH)

# 获取今天的日期 格式2019-08-01
TODAY_DATE = str(datetime.date.today())


def init_log():
    """
    func: 初始化日志，只需要在主函数中初始化一次
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    handler = logging.FileHandler(
        LOGFILE_PATH + TODAY_DATE + '.log', 'a', 'utf-8')
    formatter = logging.Formatter(
        '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    logging.info('logging module init is ok')


def clean_old_log():
    """
    删除除今天以外的日志
    """
    # 遍历目录下的所有日志文件 i是文件名
    for i in os.listdir(LOGFILE_PATH):
        if i != TODAY_DATE + '.log':
            os.remove(LOGFILE_PATH + i)
