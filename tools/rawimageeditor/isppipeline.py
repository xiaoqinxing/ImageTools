import tools.rawimageeditor.isp as isp
import tools.rawimageeditor.debayer as debayer
from tools.rawimageeditor.rawImage import RawImageInfo, RawImageParams
from ui.customwidget import critical
from imp import reload

pipeline_dict = {
    "raw":          isp.get_src_raw_data,
    "original raw": isp.get_src_raw_data,
    "black level":  isp.black_level_correction,
    "BLC":          isp.black_level_correction,
    "rolloff":      None,
    "ABF":          None,
    "demosaic":     debayer.demosaic,
    "awb":          isp.channel_gain_white_balance,
    "AWB":          isp.channel_gain_white_balance,
    "ccm":          None,
    "CCM":          None,
    "gamma":        isp.gamma_correction,
    "LTM":          isp.ltm_correction,
    "advanced chroma enhancement":  None,
    "ACE":                          None,
    "wavelet denoise":              None,
    "WNR":                          None,
    "adaptive spatial filter":      None,
    "ASF":                          None,
    "bad pixel correction":         isp.bad_pixel_correction
}

class IspPipeline():
    def __init__(self, parmas, process_bar=None):
        self.old_pipeline = []
        self.pipeline = []
        # self.data = RawImageInfo()
        self.params = parmas
        # img_list存储了pipeline中途所有的图像
        # img_list长度比pipeline长1
        self.img_list = [RawImageInfo()]
        self.process_bar = process_bar

    def reload_isp(self):
        reload(isp)
        reload(debayer)
        self.params.need_flush = True
        if (self.process_bar is not None):
            self.process_bar.setValue(0)

    def set_pipeline(self, pipeline):
        self.old_pipeline = self.pipeline
        self.pipeline = pipeline

    def pipeline_clear(self):
        self.old_pipeline = self.pipeline
        self.pipeline = []

    def pipeline_reset(self):
        """
        重新开始一个pipeline，把以前的图像清除
        """
        if(len(self.img_list) > 1):
            self.img_list = [RawImageInfo()]
            self.old_pipeline = []
            self.pipeline = []
            return True
        return False

    def add_pipeline_node(self, node):
        """
        function: 为pipeline添加一个节点
        输入是pipeline_dict的字符串
        """
        if(node in pipeline_dict):
            self.pipeline.append(node)

    def get_pipeline_node_index(self, node):
        """
        返回该node在pipeline的index
        """
        if(node in pipeline_dict and node in self.pipeline):
            return self.pipeline.index(node)

    def compare_pipeline(self):
        """
        function: 对比新老pipeline的区别
        如果不同的话，会返回一个index，表示从第index个值开始不一样的,注意这个index可能不存在于老的pipeline中
        如果相同的话，会返回0
        """
        for i, node in enumerate(self.pipeline):
            if(i > len(self.old_pipeline) - 1 or node != self.old_pipeline[i]):
                return i
        return -1

    def check_pipeline(self):
        """
        检查pipeline，如果有不同的，修改img_list
        ret: 如果pipeline不需要修改，就返回None，如果需要修改，就返回需要修改的pipeline
        """
        if(self.params.need_flush == False):
            index = self.compare_pipeline()
            if(index != -1):
                self.remove_img_node_tail(index + 1)
                return self.pipeline[index:]
            return None
        else:
            self.remove_img_node_tail(1)
            self.params.need_flush = False
            return self.pipeline
    
    def run_node(self, node, data):
        # 这里进行检查之后，后续就不需要检查了
        if(data is not None and self.params is not None and data.data is not None):
            return pipeline_dict[node](data, self.params)
        elif(self.params is None):
            self.params.set_error_str("输入的参数为空")
            return None
        elif (data.data is None):
            self.params.set_error_str("输入的图片是空")
            return None

    def run_pipeline(self):
        """
        运行pipeline，process_bar是用于显示进度的process bar
        """
        pipeline = self.check_pipeline()
        if (self.process_bar is not None):
            self.process_bar.setValue(0)

        if (pipeline is not None):
            length = len(pipeline)
            i = 1
            params = self.params
            for node in pipeline:
                data = self.img_list[-1]
                ret_img = self.run_node(node, data)
                if(ret_img is not None):
                    self.img_list.append(ret_img)
                else:
                    critical(params.get_error_str())
                    break
                if (self.process_bar is not None):
                    self.process_bar.setValue(i / length * 100)
                    i += 1
        else:
            if (self.process_bar is not None):
                self.process_bar.setValue(100)

    def get_pipeline(self):
        return self.pipeline

    def update_pipeline(self, pipeline):
        self.pipeline = pipeline

    def remove_img_node_tail(self, index):
        """
        function: 去除>=index之后的node
        """
        while index < len(self.img_list):
            self.img_list.pop()

    def get_image(self, index):
        """
        获取pipeline中的一幅图像
        如果输入-1，则返回最后一幅图像
        """
        if (index < len(self.img_list) and index >= 0):
            return self.img_list[index]
        elif (index < 0):
            return self.img_list[len(self.pipeline)+1 + index]
        else:
            return None
