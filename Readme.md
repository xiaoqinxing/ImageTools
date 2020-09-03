# ImageTools
集合了多个图像工具，扩展性好。目前集成有看图，看rtsp视频的功能，包括了镜头计算器和抖动测试工具。

## 扩展方法
1. ui类中增加工具的界面
2. tools类中增加工具的使用方式
3. ImageTools.py中添加工具的打开方式

## vscode配置方法
### UI修改和编译
1. 安装python for QT插件
2. 在设置里面填写designer.exe的路径和pyuic的路径，然后右键ui文件，就可以对文件进行修改或者编译啦。
3. 如果想要在当前目录下生成，修改pyuic的配置为：`pyside2-uic -o ${fileDirname}/${fileBasenameNoExtension}.py`
