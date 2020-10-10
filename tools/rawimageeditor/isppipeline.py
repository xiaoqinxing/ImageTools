import tools.rawimageeditor.isp as isp
from tools.rawimageeditor.rawImage import RawImageInfo,RawImageParams

class IspPipeline():
    pipeline_dict = {
        "raw":          0,
        "black level":  1,
        "BLC":          1,
        "rolloff":      2,
        "ABF":          3,
        "demosaic":     4,
        "awb":          5,
        "AWB":          5,
        "ccm":          6,
        "CCM":          6,
        "gamma":        7,
        "LTM":          8,
        "advanced chroma enhancement":  9,
        "ACE":                          9,
        "wavelet denoise":              10,
        "WNR":                          10,
        "adaptive spatial filter":      11,
        "ASF":                          11
    }

    def __init__(self):
        self.old_pipeline = [0]
        self.pipeline = [0]
        self.calc_data = []
        # self.data = RawImageInfo()
        self.params = RawImageParams()
        # img_list存储了pipeline中途所有的图像
        self.img_list = []
        self.img_list.append(RawImageInfo())

    def set_pipeline(self, pipeline):
        self.old_pipeline = self.pipeline
        self.pipeline = pipeline

    def pipeline_clear(self):
        self.old_pipeline = self.pipeline
        self.pipeline = [0]

    def add_pipeline_node(self, node):
        """
        function: 为pipeline添加一个节点
        输入是pipeline_dict的字符串
        """
        if(node in self.pipeline_dict):
            self.pipeline.append(self.pipeline_dict[node])

    def get_pipeline_node_index(self, node):
        """
        返回该node在pipeline的index
        """
        if(node in self.pipeline_dict and self.pipeline_dict[node] in self.pipeline):
            return self.pipeline.index(self.pipeline_dict[node])+1

    def compare_pipeline(self):
        """
        function: 对比新老pipeline的区别
        如果不同的话，会返回一个index，表示从第index个值开始不一样的,注意这个index可能不存在于老的pipeline中
        如果相同的话，会返回0
        """
        for i, node in enumerate(self.pipeline):
            if(i > len(self.old_pipeline) - 1 or node != self.old_pipeline[i]):
                return i
        return 0
    
    def check_pipeline(self):
        """
        检查pipeline，如果有不同的，修改img_list
        ret: 如果pipeline不需要修改，就返回true，如果需要修改，就返回false
        """
        index = self.compare_pipeline()
        if(index != 0):
            self.remove_img_node_tail(index)
            return False
        return True
    
    def run_pipeline(self):
        if(self.check_pipeline() == False):
            for node,data in zip(self.pipeline,self.img_list):
                self.img_list.append(self.run_node(node, data))
    
    def run_node(self, node, data):
        if(node == self.pipeline_dict["BLC"]):
            return isp.black_level_correction(data,self.params)
        elif(node == self.pipeline_dict["awb"]):
            return isp.channel_gain_white_balance(data,self.params)
        elif(node == self.pipeline_dict["raw"]):
            return data

    def get_pipeline(self):
        return self.pipeline

    def update_pipeline(self, pipeline):
        self.pipeline = pipeline
    
    def add_img_nodes(self, num):
        for i in range(num):
            self.img_list.append(RawImageInfo())
    
    def add_img_node(self, img):
        self.img_list.append(img)
    
    def remove_img_node_tail(self, index):
        """
        function: 去除>=index之后的node
        """
        while index < len(self.img_list):
            self.img_list.pop()
    
    def get_image(self, index):
        """
        获取pipeline中的一幅图像
        """
        if (index < len(self.img_list)):
            return self.img_list[index]
        else:
            return None