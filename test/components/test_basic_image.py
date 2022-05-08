from os.path import samefile, isfile
from components.BasicImage import ImageBasic
from components.status_code_enum import StatusCode
import operator


def test_status_code():
    ret = StatusCode.OK
    if ret is StatusCode.OK:
        assert True

    ret = StatusCode.FILE_NOT_FOUND
    if ret is StatusCode.OK:
        assert '文件不存在' == StatusCode.FILE_NOT_FOUND.value
        assert StatusCode.FILE_NOT_FOUND.name == 'FILE_NOT_FOUND'


class TestBasicImage:
    def test_load_imagefile(self):
        img = ImageBasic()
        ret = img.load_imagefile("test/resource/5.jpg")
        assert ret is StatusCode.FILE_NOT_FOUND
        ret = img.load_imagefile("test/resource/1.jpg")
        assert ret is StatusCode.OK

    def test_save_and_remove_file(self):
        img = ImageBasic()
        ret = img.save_image("test/resource/1-1.jpg")
        assert ret is StatusCode.IMAGE_IS_NONE

        ret = img.load_imagefile("test/resource/1.jpg")
        assert ret is StatusCode.OK
        ret = img.save_image("test/resource/1-1.jpg")
        assert ret is StatusCode.OK
        assert isfile("test/resource/1-1.jpg")

        ret = img.remove_image()
        assert ret is StatusCode.OK
        assert isfile("test/resource/1.jpg") is False
        assert img.img is None

        ret = img.load_imagefile("test/resource/1-1.jpg")
        assert ret is StatusCode.OK
        ret = img.save_image("test/resource/1.jpg")
        assert ret is StatusCode.OK
        assert isfile("test/resource/1.jpg")
        ret = img.remove_image()
        assert ret is StatusCode.OK
        assert isfile("test/resource/1.jpg")
        assert img.img is None

    def test_next_photo(self):
        img = ImageBasic()
        ret = img.load_imagefile("test/resource/2.jpg")
        assert ret is StatusCode.OK

        next_photo_name, index, files_nums = img.find_next_time_photo(1)
        assert samefile(next_photo_name, "test/resource/3.png")
        assert index == 3
        assert files_nums == 5

        next_photo_name, index, files_nums = img.find_next_time_photo(-1)
        assert samefile(next_photo_name,
                        "test/resource/星空背景 绘画 夜空 4k壁纸_彼岸图网.jpg")
        assert index == 1
        assert files_nums == 5

        ret = img.load_imagefile("test/resource/3.png")
        assert ret is StatusCode.OK
        next_photo_name, index, files_nums = img.find_next_nat_photo(1)
        assert samefile(next_photo_name, "test/resource/6月壁纸.jpg")
        assert index == 3
        assert files_nums == 5

        next_photo_name, index, files_nums = img.find_next_nat_photo(-1)
        assert samefile(next_photo_name, "test/resource/2.jpg")
        assert index == 1
        assert files_nums == 5

    def test_get_img_point(self):
        img = ImageBasic()
        ret = img.load_imagefile("test/resource/2.jpg")
        assert ret is StatusCode.OK
        point = img.get_img_point(214, 190)
        assert (point == [218, 211, 255]).all()

        ret = img.load_imagefile("test/resource/3.png")
        assert ret is StatusCode.OK
        point = img.get_img_point(217, 197)
        assert (point == [241, 192, 190]).all()
