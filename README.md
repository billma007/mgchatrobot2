# mgchatrobot2

A robot using open API with python

一款使用公共API进行人工智能语音聊天的机器人程序

## 1.使用/How to use?

```shell
git clone https://github.com/billma007/mgchatrobot2.git
```

克隆到本地以后需要安装第三方库。在clone的目录下面打开cmd输入：

After cloning it,you need pip some requirements:

```shell
pip install -r requirements.txt
```

**这里需要注意：如果你手动安装库，pyttsx3库需要2.72版本（pip install pyttsx3==2.72），否则会报错**

**Warning: pyttsx3 needs 2.72.Otherwise, the interpreter will report an error.**

## 2.架构/What's this?

你会看到如下文件:/you will see:

- main.py  ------包含完整功能
- easy.py  ------最简单的代码，方便理解与移植
- settings.txt -------这玩意一定要有，里面写什么无所谓，但一定要有!编译完成后的EXE文件下面也要放一个！
- requirements.txt ------依赖库

## LICENSE

MIT LICENSE 
