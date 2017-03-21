## 练习13--参数，解压，变量
在这个练习中，我们会涉及不止一个输入变量到脚本的方法。（我们会把`.py`文件叫做脚本）你知道ex13.py是怎样通过`python ex13.py`来运行的么？ 其实`ex13.py`就是这条命令的**参数**, 接下来这个练习我会详细地解释它。  

> from sys import argv  

在这行代码中，有一个叫`import`的东西，当你为Python脚本增加**功能**时，你需要从Python功能集合里调用。Python功能集合里边有很多库，但它不会每次全部加载给你，而是让你按需调用。这个设计能使你的程序保持轻盈，而且程序更具有可读性。  
`argv`全称是`arguments variable`，是一个非常标准，在很多种编程语言中都采用的命名。这个变量可以保留你在运行Python命令时输入的参数。
>script, first, second, third = argv

这代码的作用是**解压**`argv`，（目前没有比**解压**更好的词汇来描述了），效果就好像：不论python命令后面跟了什么参数，都装进`argv`，解压，然后分配给左边的那些变量。  

其实**features(功能)**这个术语并不严谨，程序员都叫它**: modules(模块)**或者**libraries(库)**.   
```
$ python ex13.py
Traceback (most recent call last):
 File "ex13.py", line 3, in <module> script, first, second, third = argv
ValueError: need more than 1 values to unpack
```
上面这段报错，很常见，因为你输入命令的时没有添加足够的参数，你像往常一样，输入：
>$ python ex13.py

`python`后面只有一个参数，还差3个参数，只要补齐就行，输入什么都可以。  
### 课程训练
1. 试着写两个程序，一个设置更少的变量，一个设置更多的变量。
2. 把raw_input 和 argv 混合使用，让终端用户来输入更多指令。
3. 记住`modules`,`modules`,`modules`,重要的事情说三遍，真是中西通用。
