## 练习41 学会讲"面向对象"
在这节练习中,我会教你怎么说`面向对象`,通过给一些术语和句子的定义,帮你理解它.最后,你需要完成一个大型的练习,从而将那这些句子固化到你的脑海里.
### 词汇训练
* `class`--告诉 Python 去做一种新东西
* `object`--两个含义:最基础的东西;任何关于某种东西的实例
* `instance`--当你告诉 Python 创建一个`class`的时候,你获得的东西
* `def`--在` class`中定义一个函数
* `self`--插入一个函数到` class`中,` self`是一个可访问的实例或对象的变量
* `inheritance`--这个概念指一个` class`可以继承另一个` class`的特点.类似你和你父母的关系
* `composition` -- 这个概念是指一个` class`可以作为另一个`class`的部分.类似于,汽车拥有轮子
* `attribute`--指的是一个` class`的性质,往往来自它的成分,并且常常是变量.
* `is-a--A` 这个短语指的是某样东西继承自另一个,比如"鲑鱼"是"鱼"
* `has-a--A` 这个短语指的是某样东西具有一个特点,或者被某个事物组成,比如"鲑鱼"都有"嘴巴".

花点时间为上述术语制作卡片,帮助记忆.

### 短语训练
接下来,我有一个 Python 代码片段的列表,以及对应的解释  
* **class X(Y)** : 制作一个 class 命名为 X is a Y
* **class X(object):def__init__(self,J)**: class has-a __init__ 并设置2个参数, self 和 J
* **class X(object): def M(self,J)**: class has-a 函数,命名为 **M** 并且拥有2个参数 self 和 J
* **foo = X()**: 为 **class X** 设置一个实例 foo
* **foo.M(J)**: 从 foo 获取** M** 函数,并用参数 self,J 调用它
* **foo.K = Q**: 从 foo 获取** K*属性,并赋给**Q**

在上述每一个示例中,你看到的**X,Y,M,J,K,Q,foo**都可以用看做空白标点.所以上面那些句子也可以换个写法:
1. make  a class named ??? that is-a Y
2. class ??? has-a __init__ that takes self and ??? parameters.
3. class ??? has-a function named ??? that takes self and ??? parameters
4. Set foo to an instance of class ???
5. from foo get the ??? function,and call it with self =?? and parameters ???
6. from foo get the ??? attribute and set it to ???

同样地,制作卡片,反复训练,把 Python 代码片段写到正面,然后把句子写到侧面,看到正面,说出反面.

### 混合练习
最后为你准备的练习是混合词汇和短语的训练,你需要做:
1. 取一张 短语卡片 开始训练
2. 反转它,阅读背面的句子,并找出句子中的每个术语,翻出对应卡片
3. 开始术语卡片开始训练
4. 坚持训练,感到无聊了就歇一会,然后重新开始

### 一项阅读训练
这有一个简单的脚本,你应该能够搞明白它,整个脚本就做了一件事,使用一个叫做` urllib`的库下载一个术语列表.
