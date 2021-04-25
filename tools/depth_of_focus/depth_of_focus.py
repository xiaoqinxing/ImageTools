import matplotlib.pyplot as plt
from tools.depth_of_focus.field_depth_window import Ui_FieldDepthWindow
from tools.depth_of_focus.LenParameters import LenParameters, SettingParamters, cmos_size_dist
from components.customwidget import MatplotlibLayout, ParamsTable
from components.window import SubWindow


class FieldDepthWindow(SubWindow):
    def __init__(self, name='FieldDepthWindow', parent=None):
        super().__init__(name, parent, Ui_FieldDepthWindow())
        [self.params, self.setting] = self.load_params(
            [LenParameters(), SettingParamters()])
        self.init_params_range()

    def show(self):
        super().show()
        self.ui.pushButton.clicked.connect(self.finished_plot_cb)
        self.ui.sensor_size.editingFinished.connect(self.coms_size_changed_cb)
        self.ui.confusion_circle_diam_slide.sliderMoved.connect(
            self.confusion_circle_diam_changed_cb)
        self.ui.sensor_size_list.currentTextChanged.connect(
            self.coms_size_list_changed_cb)

        self.set_ui_params()

        self.plot_fig = MatplotlibLayout(self.ui.plotview)
        self.tableWidget = ParamsTable(self.ui.plotview)
        self.finished_plot_cb()

    def init_params_range(self):
        self.params.aperture_range[0] = self.params.aperture/2
        self.params.aperture_range[1] = self.params.aperture*2
        self.params.focus_distance_range[0] = self.params.focus_distance/2
        self.params.focus_distance_range[1] = self.params.focus_distance*2
        self.params.focus_range[0] = self.params.focus_length/2
        self.params.focus_range[1] = self.params.focus_length*2

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

    def plot_params(self):
        self.tableWidget.clean()
        self.tableWidget.append("视场角", str(self.params.calc_fov()), '度')
        self.tableWidget.append("等效焦距", str(
            self.params.calc_equivalent_focus_length()), 'mm')
        self.tableWidget.append("超焦距距离", str(
            self.params.calc_hyperfocal_distance()/1000), 'm')
        self.tableWidget.append("前景深", str(
            self.params.calc_front_field_depth()/1000), 'm')
        self.tableWidget.append("后景深", str(
            self.params.calc_back_field_depth()/1000), 'm')
        self.tableWidget.append("总景深", str(
            self.params.calc_field_depth()/1000), 'm')
        self.tableWidget.show()

    def calc_len_params(self):
        # print('视场角：'+str(self.params.calc_fov())+'度')
        # print('等效焦距：'+str(self.params.calc_equivalent_focus_length())+'mm')
        # print('超焦距距离：'+str(self.params.calc_hyperfocal_distance()/1000) + 'm')
        # print("前景深："+str(self.params.calc_front_field_depth()/1000) + 'm')
        # print("后景深："+str(self.params.calc_back_field_depth()/1000) + 'm')
        # print("总景深：" + str(self.params.calc_field_depth()/1000)+'m')
        return

    # get params
    def get_ui_params(self):
        # basic setting
        self.params.focus_length = float(self.ui.focus_length.value())
        self.params.confusion_circle_diam = float(
            self.ui.confusion_circle_diam.value())
        self.params.aperture = float(self.ui.aperture.value())
        self.params.focus_distance = float(self.ui.focus_distance.value())*1000
        self.params.cmos_size = float(self.ui.sensor_size.value())
        # input setting
        self.setting.input_focus_length = self.ui.input_focus_length.isChecked()
        self.setting.input_apeture = self.ui.input_apeture.isChecked()
        self.setting.input_distance = self.ui.input_distance.isChecked()
        # output setting
        self.setting.output_field_depth = self.ui.output_field_depth.isChecked()
        self.setting.output_image_distance = self.ui.output_image_distance.isChecked()
        self.setting.output_params = self.ui.output_params.isChecked()
        # advanced setting
        self.params.aperture_range[0] = float(
            self.ui.apeture_min_range.value())
        self.params.aperture_range[1] = float(
            self.ui.apeture_max_range.value())
        self.params.focus_distance_range[0] = float(
            self.ui.distance_min_range.value())*1000
        self.params.focus_distance_range[1] = float(
            self.ui.distance_max_range.value())*1000
        self.params.focus_range[0] = float(self.ui.focus_min_range.value())
        self.params.focus_range[1] = float(self.ui.focus_max_range.value())

    def set_ui_params(self):
        # basic setting
        self.ui.focus_length.setValue(self.params.focus_length)
        self.ui.confusion_circle_diam.setValue(
            self.params.confusion_circle_diam)
        self.ui.aperture.setValue(self.params.aperture)
        self.ui.focus_distance.setValue(self.params.focus_distance / 1000)
        self.ui.sensor_size.setValue(self.params.cmos_size)

        # input setting
        self.ui.input_focus_length.setChecked(self.setting.input_focus_length)
        self.ui.input_apeture.setChecked(self.setting.input_apeture)
        self.ui.input_distance.setChecked(self.setting.input_distance)
        # output setting
        self.ui.output_field_depth.setChecked(self.setting.output_field_depth)
        self.ui.output_image_distance.setChecked(
            self.setting.output_image_distance)
        self.ui.output_params.setChecked(self.setting.output_params)

        # advanced setting
        self.ui.apeture_min_range.setValue(self.params.aperture_range[0])
        self.ui.apeture_max_range.setValue(self.params.aperture_range[1])
        self.ui.distance_min_range.setValue(
            self.params.focus_distance_range[0]/1000)
        self.ui.distance_max_range.setValue(
            self.params.focus_distance_range[1]/1000)
        self.ui.focus_min_range.setValue(self.params.focus_range[0])
        self.ui.focus_max_range.setValue(self.params.focus_range[1])

    # CALLBACKS
    def finished_plot_cb(self):
        self.get_ui_params()
        if self.setting.output_field_depth == True:
            self.tableWidget.clean()
            self.plot_figure()
        elif self.setting.output_params == True:
            self.plot_fig.clean()
            self.plot_params()
        self.calc_len_params()

    def coms_size_list_changed_cb(self):
        self.params.cmos_size = cmos_size_dist[self.ui.sensor_size_list.currentText(
        )]
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
