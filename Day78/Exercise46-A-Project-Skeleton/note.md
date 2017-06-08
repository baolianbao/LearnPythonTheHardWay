## 练习46-一个项目框架
这是一个关于如何创建一个优秀项目骨架的目录,这个骨架目录有你运行一个项目所需要的所有基本要素.比如项目规划,自动化测试,模块化,安装脚本等.当你开始做一个新项目时,只需要拷贝这个目录然后起个新名字,编辑文件就可以启动了.  

### 安装 Python 程序包
本节练习开始之前,你需要安装一些Python 软件,通常我们使用一个工具,叫做` pip`,来安装一些新模块.新手们面临一个问题是安装工具和安装方法太多,如果我一个一个详细讲解,花10页也写不完.所以我打算把常用的几种告诉你,然后你自己琢磨.  
安装下列 Python 工具包:
1. `pip` from http://pypi.python.org/pyp/pip
2. `distribute` from http://pypi.python.org/pypi/distribute
3. `nose` from http://pypi.pyhton.org/pypi/nose
4. `virtualenv` from http://pypi.python.org/pypi/virtualenv  

不要只是顺手下载-安装这些数据包,你应该看看别人推荐你安装的这些数据包是如何适配你的特殊系统版本的.对于 `Linux`,`OSX`,尤其是` Windows`等系统来说,安装流程是完全不同的.  
我警告你的是,这个环节是非常令人沮丧的.在商业上,我们叫它`yak shaving`.意思是指某种让人脑袋抽筋的,超级无聊的,冗长乏味的活动.你想做一个很酷的项目,但是你必须得现有个项目骨架,你想有一个项目骨架,就必须先安装某些数据包,你想安装数据包,就必须先安装数据包安装工具.你想安装这些工具,就必须搞明白你的系统适合安装哪种工具.以及怎么安装.事情的顺序就是这样...  
这是每个程序员的必经之路,在制作那些酷炫项目之前,得先干无聊乏味,闹人的工作.  
>**注意:** 有时候由于Python 安装器未将 "C:\Python27\Script "添加到系统路径,会出现错误.你只需要输入[Environment]::SetEnvironmentVariable("Path",
     "$env:Path;C:\Python27\Scripts", "User")  


### 创建项目骨架目录
首先,使用以下命令,创建你的项目骨架目录:  
```py
$ mkdir projects
$ cd projects
$ mkdir skeleton
$ cd skeleton
$ mkdir bin
$ mkdir NAME
$ mkdir tests
$ mkdir docs
```
其中 NAME 这个文件可以以你的主要模块来命名.
接下来,我们设置一些初始文件:  
```py
$ touch NAME/__init__.py
$ touch tests/__init__.py
```
在 windows PowerShell 中可以用如下命令:
```py
$ new-item -type file NAME/__init__.py
$ new-item -type file tests/__init__.py
```
我们需要创建一个` setup.py` 文件,我们后面用它来安装我们的项目.除了这个文件,我们还需要一个小的测试文件.`tests/NAME_tests.py`  
目前的项目文件结构是这样的:
```
$ ls -R
NAME	bin	docs	tests

./NAME:
__init__.py

./bin:

./docs:

./tests:
NAME_tests.py	__init__.py
```
### 使用这个框架
现在已经基本完成了准备工作,不论任何时候当你想开始一个新项目时,按下面清单去做就行了:
1. 复制整个框架的目录结构,起个新名字就行了
2. 用你的项目名称来命名`NAME`模块,这是个 root 模块
3. 编辑` setup.py`,替换成你的项目信息
4. 重命名` tests/NAME_tests.py`
5. 用 nosetests 检查所有文件至少两遍
6. 开始写代码  


### 必要的测验
本节练习没有**课程训练**,但是有一个测验需要完成:  
1. 阅读如何使用那些安装工具
2. 阅读` setup.py`文件,了解它能提供的信息.注意:通常这个文件内容书写的并不好,可读性差
3. 制作一个项目,为模块编写代码,使它能够工作
4. 阅读如何编写一个可运行的 Python 脚本,然后为你的` bin`目录添加 python 脚本使它能够运行
5. 需要在` setup.py`中提及` bin`的脚本,这样才能够安装
6. 使用` setup.py`安装你自己的模块.确保它能工作,最后用 pip 卸载它.
