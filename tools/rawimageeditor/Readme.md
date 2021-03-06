# 图片查看工具
这是一款能够对RAW图进行解析和ISP处理的工具。可以方便的进行后期算法的验证（热更新、直观的图像显示和分析）。退出后会自动保存上次打开的窗口，以及窗口里的参数。同时将界面与处理线程分离，让界面更加流畅。

### 界面

1. 左侧是图像预览窗口
2. 右上角有两个窗口，左边的是RAW图的设置，右边的是ISP处理流程
3. 右下角是对ISP处理的一些配置

### 使用方法

1. 先进行RAW图的设置，然后可以点击“打开图片”或者拖拽的方式打开图片，此时图片预览窗口显示的是RAW图，可以用鼠标进行放大缩小和移动，窗口的左下角会显示每个点的值，以及缩放比例
2. ISP处理流程，可以通过勾选的方式去启用部分ISP流程，通过拖拽的方式去排列ISP的顺序，然后点击确定按钮，可以进行ISP的处理，右下角的进度条可以显示ISP处理的进度。
3. 右下角的ISP参数设置窗口，修改参数后，也需要点击确定按钮，运行ISP。第二步和第三步ISP的处理，会对比之前的ISP流程，自动搜索最少的处理流程。
4. 双击ISP处理流程中的模块，可以看到经过这个模块的处理，图片变成了什么效果。此功能可以方便的看到每个ISP模块的效果。
5. 如果需要进行算法的调试，修改相关ISP算法代码之后，点击`算法热更新`，可以重新加载ISP相关算法，不需要重新启动程序。
6. 目前仅实现了黑电平校正，白平衡，坏点校正、CCM颜色校正、去马赛克和局部对比度增强，后续继续完善