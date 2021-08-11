from os import startfile, mkdir
from os.path import exists, abspath, dirname
from sys import exit
from PySide2.QtWidgets import QDialog
from components.ui.check_update_win import Ui_CheckUpdate
import requests
import time
from logging import info
from PySide2.QtCore import Signal, QThread
from components.customwidget import critical
from components.property import set_persist, get_persist, IS_NEED_AUTO_UPDATE

VERSION_NUMS_LEN = 3
VERSION_FILE = 'https://imagetools.qinxing.xyz/version.md'

CURRENT_VERSION_FILE = 'version.md'
REMOTE_INSTALL_PACK = 'https://imagetools.qinxing.xyz/ImageTools.exe'
# REMOTE_INSTALL_PACK = 'https://imagetools.qinxing.xyz/ChromeSetup.exe'
DOWNLOAD_INSTALL_PACK = '.\\latest_installer\\installer.exe'


def check_is_latest(current, new) -> bool:
    """
    func: 检查是否为最新版本
    """
    current_version = current.split('.')
    new_version = new.split('.')
    for i in range(VERSION_NUMS_LEN):
        if(int(current_version[i]) < int(new_version[i])):
            return False
        if(int(current_version[i]) > int(new_version[i])):
            return True
    return True


def get_latest_version_log():
    """
    func: 获取最新的版本日志文件
    把日志转换成UTF-8格式
    """
    res = requests.get(VERSION_FILE, timeout=2)
    if res.status_code != 200:
        return ''
    res.encoding = 'utf-8'
    return res.text


def get_current_version_log():
    """
    func: 获取当前版本日志
    """
    with open(CURRENT_VERSION_FILE, 'r', encoding='utf-8') as f:
        return f.read()


def get_version(version_log):
    """
    func: 获取日志文件的最新版本号
    日志文件格式必须为 **x.x.x**
    """
    start_index = version_log.find('**')
    end_index = version_log.find('**', start_index + 1)
    return version_log[start_index + 2:end_index]


def download_file(srcUrl):
    """
    func: 下载一个大文件
    """
    localFile = srcUrl.split('/')[-1]
    info('开始下载 %s' % (srcUrl))
    startTime = time.time()
    with requests.get(srcUrl, stream=True) as r:
        contentLength = int(r.headers['content-length'])
        line = 'content-length: %dB/ %.2fKB/ %.2fMB'
        line = line % (contentLength, contentLength /
                       1024, contentLength/1024/1024)
        info(line)
        downSize = 0
        with open(localFile, 'wb') as f:
            for chunk in r.iter_content(8192):
                if chunk:
                    f.write(chunk)
                downSize += len(chunk)
                # line = '%d KB/s - %.2f MB， 共 %.2f MB'
                # line = line % (downSize/1024/(time.time()-startTime),
                #                downSize/1024/1024, contentLength/1024/1024)
                # info(line)
                if downSize >= contentLength:
                    break
        timeCost = time.time() - startTime
        info('下载成功, 共耗时: %.2f s, 平均速度: %.2f KB/s' %
             (timeCost, downSize/1024/timeCost))
    return True


def simple_check_is_need_update() -> bool:
    """
    func: 简单的返回是否需要更新
    """
    current_version = get_version(get_current_version_log())
    version_log = get_latest_version_log()
    if(version_log == ''):
        return False
    latest_version = get_version(version_log)
    if check_is_latest(current_version, latest_version) is True:
        return False
    return True


def check_update():
    """
    检查更新
    """
    current_log = get_current_version_log()
    current_version = get_version(current_log)

    version_log = get_latest_version_log()
    if(version_log == ''):
        return 'connect error', current_version, current_log

    latest_version = get_version(version_log)
    if check_is_latest(current_version, latest_version) is True:
        return 'already latest', current_version, current_log
    else:
        return latest_version, current_version, version_log


class CheckUpdate(QDialog):

    def __init__(self, parent):
        """
        func: 初始化直方图统计信息UI，把父类的指针变成选中方框模式
        """
        super().__init__(parent)
        self.ui = Ui_CheckUpdate()
        self.ui.setupUi(self)
        self.autoupdate = get_persist(IS_NEED_AUTO_UPDATE, False)
        self.ui.autoupdate.setChecked(self.autoupdate)
        self.need_update = 0
        self.ui.autoupdate.stateChanged.connect(self.set_autoupdate_param)
        self.ui.ok.clicked.connect(self.start_update)
        self.ui.cancel.clicked.connect(lambda: self.close())
        self.update_proc = UpdateProc(
            REMOTE_INSTALL_PACK, self)
        self.update_proc.doneCB.connect(self.update_proc_done)
        self.update_proc.processRateCB.connect(
            lambda rate: self.ui.progress.setValue(rate))

        latest_version, current_version, latest_log = check_update()

        # 异常处理
        if(latest_version == 'connect error'):
            self.ui.version_num.setText(
                '!!!网络连接出错!!! 当前版本为 ' + current_version)
            self.need_update = -1
        elif(latest_version == 'already latest'):
            self.ui.version_num.setText('软件已经是最新啦！当前版本为 ' + current_version)
            self.need_update = 0
        else:
            self.ui.version_num.setText(
                '有版本更新啦！当前版本为 ' + current_version + '; 最新版本为 ' + latest_version)
            self.need_update = 1

        self.ui.textBrowser.setMarkdown(latest_log)

    def set_autoupdate_param(self, p):
        self.autoupdate = (p != 0)
        set_persist(IS_NEED_AUTO_UPDATE, self.autoupdate)
        info('设置自动更新功能 {}'.format(self.autoupdate))

    def start_update(self):
        if self.need_update == 1:
            if(not exists(dirname(DOWNLOAD_INSTALL_PACK))):
                mkdir(dirname(DOWNLOAD_INSTALL_PACK))
            self.update_proc.start()
        elif self.need_update == 0:
            critical('软件已经是最新啦')
        elif self.need_update == -1:
            critical('网络连接出错')

    def update_proc_done(self, ret):
        if(ret == 0):
            info('下载成功')
            # Popen('start ' + REMOTE_INSTALL_PACK.split('/')
            #       [-1], shell=True, stdin=PIPE, stdout=PIPE)
            # os.system('start ChromeSetup.exe')
            if exists(DOWNLOAD_INSTALL_PACK) is True:
                startfile(DOWNLOAD_INSTALL_PACK)
                info('正在启用最新升级包')
                exit()
            critical('下载的升级包不存在')
        else:
            info('下载失败')


class UpdateProc(QThread):
    doneCB = Signal(int)
    processRateCB = Signal(int)

    def __init__(self, url, parent=None) -> None:
        super(UpdateProc, self).__init__(parent=parent)
        self.url = url

    def run(self):
        self.processRateCB.emit(0)
        info('开始下载更新...')
        with requests.get(self.url, stream=True, timeout=5) as r:
            contentLength = int(r.headers['content-length'])
            downSize = 0
            with open(DOWNLOAD_INSTALL_PACK, 'wb') as f:
                for chunk in r.iter_content(8192):
                    if chunk:
                        f.write(chunk)
                    downSize += len(chunk)
                    self.processRateCB.emit(downSize/contentLength * 100)
                    info('下载进度{}%'.format(downSize/contentLength * 100))
                    if downSize >= contentLength:
                        self.doneCB.emit(0)
                        return
        self.doneCB.emit(-1)
        return
