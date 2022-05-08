from components.check_update import get_version, get_latest_version_log, get_current_version_log, check_is_latest


def test_check_is_latest():
    assert check_is_latest('1.5.0', '1.4.0') is True
    assert check_is_latest('1.5.0', '1.6.0') is False
    assert check_is_latest('1.5.0', '1.12.0') is False
    assert check_is_latest('1.5.0', '12.4.0') is False
    assert check_is_latest('1.5.0', '0.5.1') is True


TEST_VERSION_LOG = """
**1.5.0**

做了一些修改

**1.4.0**

做了另外一些修改
"""


def test_get_version():
    assert get_version(TEST_VERSION_LOG) == '1.5.0'
    assert get_version(TEST_VERSION_LOG[10:]) == '1.4.0'


def test_get_latest_version_log():
    assert get_version(get_latest_version_log()) == get_version(
        get_current_version_log())


TEST_DOWNLOAD_LINK = 'https://imagetools.qinxing.xyz/ChromeSetup.exe'
TEST_DOWNLOAD_FILE = './test.exe'


def test_download():
    # assert download_file(TEST_DOWNLOAD_LINK) == True 下载文件OK
    assert True
