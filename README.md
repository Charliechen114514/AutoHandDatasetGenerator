# AutoHandDatasetGenerator V1.0

## 自动手部数据集生成器

​	本软件是为了快速生成可以给MediaPipe ModelMaker生成数据集的软件。目前，软件提供手动生成和自动生成数据集两种格式。

## 使用办法

 1. 用户首先应当确保机器上接入了可用的摄像头若干，软件将会使用Opencv-python的VedioCapture库打开您的目标摄像头进行读取。

 2. 请输入本次生成类别的Label标签，Mediapipe只需要一个表达标签的文件夹下装载目标手部的图象集即可

 3. 选取文件夹的基文件夹，所有类别的数据集将会生成在这里，以作者的一次测试为例：

    ```
    tree .
    
    - BaseDir <- select the existing dir: "BaseDir" as the base dirent
    |--open_palm 	# Auto generate
    |--closed_fist 	# Auto generate
    ```

 4. 调整想要使用的模式！自动 or 手动；自动请调整单次截图的周期，本软件支持1s - 10s

 5. 打开目标摄像头，手动模式需要进行一次点击，点击时才会截取数据集。该方式适合生成更为精良的数据集；自动模式则会按照周期一次触发截取数据集，当然，您也可以点击手动收集自行再插入数据集，而不是必须等待设定的秒数

 6. 关闭摄像头，即可前往指定的文件夹下获取数据集了

## 依赖下载

​	请参考由pipreq生成的requirements.txt使用。制作软件只用到了主要的三个依赖

```
pip install pyqt6		# 主要的Ui框架依赖
pip install mediapipe 	# 自动捕获
pip install pygrabber	# 获取机器下可用的摄像头列表
```

## 程序打包

​	如果您有自定义的打包需求，您可以参考build.md文件进行程序的打包！
