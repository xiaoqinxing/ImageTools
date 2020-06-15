import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from field_depth_ui import Ui_MainWindow
from LenParameters import LenParameters,SettingParamters,cmos_size_dist
from MatplotlibWidget import MatplotlibWidget


class App(object):
    def __init__(self):
        app = QApplication(sys.argv)
        app.setStyle('Fusion')
        window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(window)
        window.show()
        self.field_depth_figure = None
        self.image_distance_figure = None
        self.setting = SettingParamters()
        self.params = LenParameters()
        self.get_ui_params()
        self.params.show()
        self.pri_params = LenParameters()
        self.ui.pushButton.clicked.connect(self.finished_plot_cb)
        self.ui.sensor_size.editingFinished.connect(self.coms_size_changed_cb)
        self.ui.confusion_circle_diam_slide.sliderMoved.connect(
            self.confusion_circle_diam_changed_cb)
        self.ui.sensor_size_list.currentTextChanged.connect(self.coms_size_list_changed_cb)
        self.init_params_range()
        self.plot_fig = MatplotlibWidget(self.ui.gridLayout)
        self.plot_figure()
        sys.exit(app.exec_())

    def init_params_range(self):
        self.ui.apeture_min_range.setValue(self.params.aperture/2)
        self.ui.apeture_max_range.setValue(self.params.aperture*2)
        self.ui.distance_min_range.setValue(self.params.focus_distance/2000)
        self.ui.distance_max_range.setValue(self.params.focus_distance/500)
        self.ui.focus_min_range.setValue(self.params.focus_length/2)
        self.ui.focus_max_range.setValue(self.params.focus_length*2)
        self.params.aperture_range[0] = float(self.ui.apeture_min_range.text())
        self.params.aperture_range[1] = float(self.ui.apeture_max_range.text())
        self.params.focus_distance_range[0] = float(
        self.ui.distance_min_range.text())*1000
        self.params.focus_distance_range[1] = float(
            self.ui.distance_max_range.text())*1000
        self.params.focus_range[0] = float(self.ui.focus_min_range.text())
        self.params.focus_range[1] = float(self.ui.focus_max_range.text())

    def plot_figure(self):
        self.plot_fig.clean()
        if(self.setting.output_field_depth == True):
            if(self.setting.input_distance == True):
                (x, y1, y2) = self.params.calc_depth_map_from_distance()
                self.plot_fig.label("对焦距离(m)", "景深范围(m)")
            elif(self.setting.input_focus_length == True):
                (x, y1, y2) = self.params.calc_depth_map_from_focus()
                self.plot_fig.label("焦距(mm)", "景深范围(m)")
            elif(self.setting.input_apeture == True):
                (x, y1, y2) = self.params.calc_depth_map_from_apeture()
                self.plot_fig.label("光圈值(F)", "景深范围(m)")
            self.plot_fig.input_2line(x, y1, y2)
            self.plot_fig.draw()

    def calc_len_params(self):
        print('视场角：'+str(self.params.calc_fov())+'度')
        print('等效焦距：'+str(self.params.calc_equivalent_focus_length())+'mm')
        print('超焦距距离：'+str(self.params.calc_hyperfocal_distance()/1000) + 'm')
        print("前景深："+str(self.params.calc_front_field_depth()/1000) + 'm')
        print("后景深："+str(self.params.calc_back_field_depth()/1000) + 'm')
        print("总景深：" + str(self.params.calc_field_depth()/1000)+'m')

    # get params
    def get_ui_params(self):
        # basic setting
        self.params.focus_length = float(self.ui.focus_length.text())
        self.params.confusion_circle_diam = float(
            self.ui.confusion_circle_diam.text())
        self.params.aperture = float(self.ui.aperture.text())
        self.params.focus_distance = float(self.ui.focus_distance.text())*1000
        self.params.cmos_size = float(self.ui.sensor_size.text())
        # input setting
        self.setting.input_focus_length = self.ui.input_focus_length.isChecked()
        self.setting.input_apeture = self.ui.input_apeture.isChecked()
        self.setting.input_distance = self.ui.input_distance.isChecked()
        # output setting
        self.setting.output_field_depth = self.ui.output_field_depth.isChecked()
        self.setting.output_image_distance = self.ui.output_image_distance.isChecked()
        self.setting.output_params = self.ui.output_params.isChecked()
        # advanced setting
        self.params.aperture_range[0] = float(self.ui.apeture_min_range.text())
        self.params.aperture_range[1] = float(self.ui.apeture_max_range.text())
        self.params.focus_distance_range[0] = float(
            self.ui.distance_min_range.text())*1000
        self.params.focus_distance_range[1] = float(
            self.ui.distance_max_range.text())*1000
        self.params.focus_range[0] = float(self.ui.focus_min_range.text())
        self.params.focus_range[1] = float(self.ui.focus_max_range.text())

    # CALLBACKS
    def finished_plot_cb(self):
        self.get_ui_params()
        self.plot_figure()
        self.calc_len_params()

    def coms_size_list_changed_cb(self):
        self.params.cmos_size = cmos_size_dist[self.ui.sensor_size_list.currentText()]
        self.ui.sensor_size.setValue(self.params.cmos_size)
        self.confusion_circle_diam_changed_cb()

    def coms_size_changed_cb(self):
        self.params.cmos_size = self.ui.sensor_size.value()
        self.confusion_circle_diam_changed_cb()

    def confusion_circle_diam_changed_cb(self):
        value = self.ui.confusion_circle_diam_slide.value()
        self.params.confusion_circle_diam = self.params.cmos_size / \
            1000*(0.5+value/100)
        self.ui.confusion_circle_diam.setValue(
            self.params.confusion_circle_diam)


if __name__ == "__main__":
    app = App()
