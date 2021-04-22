from tools.rawimageeditor.RawImageParams import RawImageParams
from tools.rawimageeditor.RawImageInfo import RawImageInfo
import tools.rawimageeditor.ispfunction as ispfunc
from imp import reload
import time
from PySide2.QtCore import Signal, QThread
from PySide2.QtWidgets import QMessageBox
from threading import Lock

class IspPipeline():
    def __init__(self, parmas, process_bar=None):
        self.old_pipeline = []
        self.pipeline = []
        self.params = parmas
        # img_list存储了pipeline中途所有的图像
        # img_list长度比pipeline长1
        self.img_list = [RawImageInfo()]
        self.process_bar = process_bar
        self.imglist_mutex = Lock()
        self.ispProcthread = ISPProc(self.params, self.img_list, self.imglist_mutex)

    def reload_isp(self):
        """
        func: 热更新 重载ISP算法模块
        """
        reload(ispfunc.debayer)
        reload(ispfunc.isp)
        reload(ispfunc)
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
        func: 重新开始一个pipeline，把以前的图像清除
        """
        if(len(self.img_list) > 1):
            self.imglist_mutex.acquire()
            self.img_list = [RawImageInfo()]
            self.imglist_mutex.release()
            self.old_pipeline = []
            self.pipeline = []
            return True
        return False

    def add_pipeline_node(self, node):
        """
        func: 为pipeline添加一个节点
        输入是pipeline_dict的字符串
        """
        if(node.lower() in ispfunc.pipeline_dict):
            self.pipeline.append(node.lower())

    def get_pipeline_node_index(self, node):
        """
        func: 返回该node在pipeline的index, 如果不存在，就返回-1
        """
        if(node.lower() in ispfunc.pipeline_dict and node.lower() in self.pipeline):
            return self.pipeline.index(node.lower())
        else:
            return -1

    def compare_pipeline(self):
        """
        func: 对比新老pipeline的区别
        如果不同的话，会返回一个index，表示从第index个值开始不一样的,注意这个index可能不存在于老的pipeline中
        如果相同的话，会返回0
        """
        for i, node in enumerate(self.pipeline):
            if(i > len(self.old_pipeline) - 1 or node != self.old_pipeline[i]):
                return i
        return -1

    def check_pipeline(self):
        """
        func: 检查pipeline，如果有不同的，修改img_list
        ret: 如果pipeline不需要修改，就返回None，如果需要修改，就返回需要修改的pipeline
        """
        # 如果参数有修改，优先返回需要修改的pipeline
        if(self.params.need_flush == True):
            if(len(self.params.need_flush_isp) > 0):
                index = -1
                self.params.need_flush = False
                for node in self.params.need_flush_isp:
                    index = self.get_pipeline_node_index(node)
                    if(index != -1):
                        self.remove_img_node_tail(index)
                        # 需要把新老pipeline进行对比
                        index_ret = self.compare_pipeline()
                        if(index_ret != -1):
                            self.remove_img_node_tail(index_ret)
                            return self.pipeline[index_ret:]
                        else:
                            return self.pipeline[index:]
                    else:
                        return None
            else:
                self.remove_img_node_tail(0)
                self.params.need_flush = False
                return self.pipeline
        else:
            index = self.compare_pipeline()
            if(index != -1):
                self.remove_img_node_tail(index)
                return self.pipeline[index:]
            return None

    def run_pipeline(self):
        """
        func: 运行pipeline，process_bar是用于显示进度的process bar, callback是运行完的回调函数
        """
        pipeline = self.check_pipeline()
        print(pipeline)
        self.ispProcthread.set_pipeline(pipeline)
        self.ispProcthread.start()

    def remove_img_node_tail(self, index):
        """
        func: 去除>=index之后的node，由于image的长度比pipeline多1，因此需要将index+1
        """
        index += 1
        self.imglist_mutex.acquire()
        while index < len(self.img_list):
            self.img_list.pop()
        self.imglist_mutex.release()

    def get_image(self, index):
        """
        func: 获取pipeline中的一幅图像
        如果输入-1，则返回最后一幅图像
        """
        ret_img = None
        self.imglist_mutex.acquire()
        if (index < len(self.img_list) and index >= 0):
            ret_img = self.img_list[index]
        elif (index < 0 and len(self.pipeline)+1 + index < len(self.img_list)):
            ret_img = self.img_list[len(self.pipeline)+1 + index]
        self.imglist_mutex.release()
        if(ret_img is not None):
            return ret_img
        else:
            return RawImageInfo()

class ISPProc(QThread):
    doneCB = Signal() # 自定义信号，其中 object 为信号承载数据的类型
    processRateCB = Signal(int)
    costTimeCB = Signal(str)
    errorCB = Signal(str)

    def __init__(self, params, img_list, mutex:Lock, parent=None):
        super(ISPProc, self).__init__(parent)		
        self.params = params
        self.img_list = img_list
        self.pipeline = None
        self.mutex = mutex
    
    def run_node(self, node, data):
        # 这里进行检查之后，后续就不需要检查了
        if(data is not None and self.params is not None):
            return ispfunc.pipeline_dict[node](data, self.params)
        elif(self.params is None):
            self.params.set_error_str("输入的参数为空")
            return None
    
    def set_pipeline(self, pipeline):
        self.pipeline = pipeline
    
    def run(self):
        self.processRateCB.emit(0)
        if (self.pipeline is not None):
            length = len(self.pipeline)
            i = 1
            params = self.params
            start_time = time.time()
            for node in self.pipeline:
                data = self.img_list[-1]
                try:
                    ret_img = self.run_node(node, data)
                except Exception as e:
                    self.errorCB.emit("ISP算法[{}]运行错误:{}\r\n{}".format(node, params.get_error_str(),e))
                    return

                if(ret_img is not None):
                    self.mutex.acquire()
                    self.img_list.append(ret_img)
                    self.mutex.release()
                else:
                    self.errorCB.emit(params.get_error_str())
                    break
                self.processRateCB.emit(i / length * 100)
                i += 1
            stop_time = time.time()
            self.costTimeCB.emit('总耗时:{:.3f}s'.format(stop_time-start_time))
            self.doneCB.emit()
        else:
            self.processRateCB.emit(100)