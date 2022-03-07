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

**Warning: pyttsx3 needs 2.72  .Otherwise, the interpreter will report an error.**

## 2.架构/What's this?

你会看到如下文件:/you will see:

- main.py  ------包含完整功能/Full functionality included
- easy.py  ------最简单的代码，方便理解与移植/The simplest code, easy to understand and transplant
- settings.txt -------配置文件。在2.4.2Beta2版本后可以自动生成/configuration file
- requirements.txt ------依赖库/Requirements

## 3.下载已编译release版本/download

该软件的已编译exe文件(中文版)已经在release中发布了。

- 2.4.2 Developer Beta [GitHub Release](https://github.com/billma007/mgchatrobot2/releases/download/2.4.2DeveloperBeta/2.4.2beta2.exe)
- 2.4.2 Developer Beta [Github Mirror in China](https://ghproxy.com/https://github.com/billma007/mgchatrobot2/releases/download/2.4.2DeveloperBeta/2.4.2beta2.exe)

## 4.更新日志/Update log

- 2022/3/7 2.4.3 修复了`read()`函数在读入时无法识别utf-8字符的问题，将默认的gbk字符表切换成了utf-8字符
- 2022/3/6 2.4.0正式版和2.4.2Developer Beta 添加自动检测和生成settings.txt的代码，目录下没有settings.txt不会报错或者闪退了。
- 2022/3/6 2.4.1-2.4.2添加自动检测和生成settings.txt的代码，目录下没有settings.txt不会报错或者闪退了。
- 2022/3/5 2.3.0 添加settings.txt可以让用户自主选择是否开启pyttsx3语音播报
- 2022/3/4 2.2.0添加目录并给用户更多选项
- 2022/3/3 2.0.0Rewrite(2.1.0)腾空出世，将这个8行的陈旧的代码翻出来重构并重新编写，但是已经无法重现当年辉煌
- 2021/8/24 电脑坏了，而且没有提交到GitHub，花了一个月时间构建的代码全部嗝屁，只留下了8行基本代码
- 2021/8/19 2.0.0Pro版本在QQ上面适配大获成功，开始进行错误封装与代码完善
- 2021/7/31 2.0.0发布 开始在原有API基础上进行在[nonebot2](https://github.com/nonebot/nonebot2)框架下的QQ机器人适配
- 2021/7/28 1.1.0版本发布 支持pyttsx3语音播报但没法关掉
- 2021/7/24 1.0.0正式版发布 修复了闪退等大量bug
- 2021/7/19 1.0.0Developer Beta2发布 进行少量内部人员测试
- 2021/7/17 1.0.0Developer Beta发布 支持基本的智能聊天
- 2021/7/14 1.0.0版本开始编写
- 2021/7/1 开始放暑假，开始构思并查找资料

## 5.关于作者/About

江苏省苏州市的一个普通高中牲，一个在省赛就被刷下来的信息学奥林匹克竞赛选手，热爱编程，但不喜欢前端。

欢迎通过以下联系方式与我探讨信息竞赛、博客搭建、学术讨论以及扯皮：

- QQ:36937975
- Twitter:@billma6688
- Facebook/Instagram:billma007
- CodeForces/USACO/AtCoder:billma007(不常用/not use them usually)

## 推广：个人博客/Blog

[欢迎来到我的博客/Welcome Here!](https://billma.top)

## LICENSE

[MIT LICENSE](LICENSE)
