import numpy as np
import math


class LenParameters(object):
    def __init__(self):
        '''
        @focus_length: 实际焦距(单位mm)
        @aperture: 光圈(F)
        @focus_distance: 对焦距离(单位mm)
        @effective_focus_length: 有效焦距(单位mm)
        @confusion_circle_diam: 弥散圈直径(单位mm)
        @cmos_size: sensor尺寸(单位mm)
        '''
        self.focus_length = 0
        self.aperture = 0
        self.focus_distance = 0
        self.effective_focus_length = 0
        self.focus_distance_range = [0, 0]
        self.aperture_range = [0, 0]
        self.focus_range = [0, 0]
        self.confusion_circle_diam = 0
        self.cmos_size = 0

    def show(self):
        '''
        调试打印
        '''
        print('=========================================')
        print('实际焦距: ' + str(self.focus_length) + ' mm')
        print('光圈: F/' + str(self.aperture))
        print('对焦距离: ' + str(self.focus_distance) + ' mm')
        print('有效焦距: ' + str(self.effective_focus_length) + ' mm')
        print('弥散圈直径: ' + str(self.confusion_circle_diam) + ' mm')
        print('=========================================')

    def calc_front_field_depth(self):
        """
        计算前景深，有两种方法：本文用的https://wenku.baidu.com/view/2191302baf45b307e9719706.html的方法，更加准确一点
        """
        # a = self.aperture*self.confusion_circle_diam * \
        #     self.focus_distance*self.focus_distance
        # b = self.focus_length*self.focus_length + self.aperture * \
        #     self.confusion_circle_diam*self.focus_distance
        a = self.focus_length*self.focus_length*self.focus_distance
        b = self.focus_length*self.focus_length + \
            (self.focus_distance - self.focus_length) * \
            self.aperture*self.confusion_circle_diam
        return (a/b)

    def calc_back_field_depth(self):
        """
        计算后景深
        """
        # a = self.aperture*self.confusion_circle_diam * \
        #     self.focus_distance*self.focus_distance
        # b = self.focus_length*self.focus_length - self.aperture * \
        #     self.confusion_circle_diam*self.focus_distance
        a = self.focus_length*self.focus_length*self.focus_distance
        b = self.focus_length*self.focus_length - \
            (self.focus_distance - self.focus_length) * \
            self.aperture*self.confusion_circle_diam
        ret = a/b
        # 防止后景深计算为负数
        if(ret <= 0):
            ret = float('inf')
        return ret

    def calc_confusion_circle_diam(self):
        '''
        通过CMOS的尺寸计算弥散圈直径，默认是CMOS对角线尺寸除1000
        '''
        self.confusion_circle_diam = self.cmos_size/1000
        return self.confusion_circle_diam

    def calc_image_distance(self, step=10, unit=1000):
        '''
        计算不同物距范围内的像距
        '''
        y = list()
        x = range(self.focus_distance_range[0],
                  self.focus_distance_range[1], step*10)
        for self.focus_distance in x:
            y.append((self.focus_distance*self.focus_length) /
                     (self.focus_distance-self.focus_length))
        return (x, y)

    def calc_field_depth(self):
        '''
        计算总景深，后景深减去前景深
        '''
        return (self.calc_back_field_depth() - self.calc_front_field_depth())

    def calc_fov(self):
        '''
        计算对角线视场角
        '''
        image_distance = (self.focus_distance*self.focus_length) / \
            (self.focus_distance-self.focus_length)
        alpha = math.atan((self.cmos_size/2)/image_distance)
        return (2*alpha*180/math.pi)

    def calc_equivalent_focus_length(self):
        '''
        计算等效焦距
        '''
        return (43.27/self.cmos_size*self.focus_length)

    def calc_hyperfocal_distance(self):
        '''
        计算超焦距，刚好后景深是无穷远时的对焦距离
        '''
        return (self.focus_length*self.focus_length/self.aperture/self.confusion_circle_diam+self.focus_length)

    def calc_depth_map_from_distance(self, step_num=1000, unit=1000):
        '''
        计算不同物距范围内的景深
        '''
        y1 = list()
        y2 = list()
        x = np.linspace(self.focus_distance_range[0],
                        self.focus_distance_range[1], step_num)
        for self.focus_distance in x:
            y1.append(self.calc_front_field_depth())
            y2.append(self.calc_back_field_depth())
        y1 = np.array(y1)/unit
        y2 = np.array(y2)/unit
        x = np.array(x)/unit
        return (x, y1, y2)

    def calc_depth_map_from_focus(self, step_num=1000, unit=1000):
        '''
        计算不同焦距范围内的景深
        '''
        y1 = list()
        y2 = list()
        x = np.linspace(self.focus_range[0],
                        self.focus_range[1], step_num)
        for self.focus_length in x:
            y1.append(self.calc_front_field_depth())
            y2.append(self.calc_back_field_depth())
        y1 = np.array(y1)/unit
        y2 = np.array(y2)/unit
        x = np.array(x)
        return (x, y1, y2)

    def calc_depth_map_from_apeture(self, step_num=1000, unit=1000):
        '''
        计算不同光圈范围内的景深
        '''
        y1 = list()
        y2 = list()
        x = np.linspace(self.aperture_range[0],
                        self.aperture_range[1], step_num)
        for self.aperture in x:
            y1.append(self.calc_front_field_depth())
            value = self.calc_back_field_depth()
            # 防止后景深计算为负数
            if(value <= 0):
                value = float('inf')
            y2.append(value)
        y1 = np.array(y1)/unit
        y2 = np.array(y2)/unit
        x = np.array(x)
        return (x, y1, y2)


class SettingParamters(object):
    def __init__(self):
        # input setting
        self.input_focus_length = False
        self.input_apeture = False
        self.input_distance = False
        # output setting
        self.output_field_depth = False
        self.output_image_distance = False
        self.output_params = False


cmos_size_dist = {
    "1/6": 3.0,
    "1/4": 4.0,
    "1/3.6": 5.0,
    "1/3.2": 5.678,
    "1/3": 6.0,
    "1/2.8": 6.46,
    "1/2.7": 6.592,
    "1/2.5": 7.182,
    "1/2": 8.000,
    "1/1.8": 8.933,
    "1/1.7": 9.500,
    "1/1.6": 10.07,
    "2/3": 11.00,
    "1": 16.0,
    "4/3": 22.5,
    "1.8": 25.878,
    "35mm film": 43.267
}
