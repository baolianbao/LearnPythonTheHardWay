## 练习40-模块,类,以及对象
Python 就是那种面向编程的语言,它意味Python 用叫做`类`的东西来构建代码,能让你通过特殊的方式来组织代码. 使用`类`,你可以增强代码的一致性,让代码运行的干净利落.至少理论上这样.  

我将会利用你已经学过的字典和模块的知识,开始教你认识面向对象编程,类,和对象.我的顾虑是面向对象这个概念有点反常识,你可能一时半会理解不了,没关系,试着去理解我说的每一句话,敲代码,在下个练习我们会搞定它.  

我们开始吧:

### 模块就像字典
你知道怎样创建并使用一个字典,就是用一个东西映射另一个东西. 即如果你有个字典的关键字` apple`,你想获得它的内容,你需要这样做:  
```py
 mystuff = {'apple': "I AM APPLES!"}
  print mystuff['apple']
```
可以概括为" 从 Y 中获取 X", 现在思考 一下`modules`,目前为止你已经使用过好几次了,根据下面的流程:
1. 你知道一个` module`就是一个 Python 文件,里面有一些函数或者变量
2. 接着导入Python 文件
3. 然后你可以使用草怎是`.`访问文件中的函数和变量

假设我有一个` module`,我决定命名为` mystuff.py`,然后放一个函数`apple`,这个` module`应该是下面这个样子:
```py
# this goes in mystuff.py
def apple():
    print "I AM APPLES!"
```
一旦创建好,我就可以` import`这个` module`,访问` apple函数`:
```py
import mystuff
mystuff.apple()

我还可以放一个变量,命名为` tangerine`,比如这样:
```py
def apple():
  print "I AM APPLES!"
#this is just a variable
tangerine = "Living reflection of a dream"
# 然后我可以访问这个变量
import mystuff

mystuff.apple()
print mystuff.tangerine
```
话题回到"字典",你应该好好观察一下这两者的用法是多么相似.不过语法是不同的,我们对比一下:
>mystuff['apple'] # 这是字典的语法  
>mystuff.apple()# 这是模块的用法  
>mystuff.tangerine # 相同点,这只一个变量

这意味着我们掌握了一个 Python 的通用模板:
1. 创建一个` key = value`格式的容器
2. 通过` key`的名字,从容器里拿东西

在字典的例子中,`key`是字符串,语法是`[ key]`,在模块的例子中,`key`是个标识,语法是`. key`,其他的内容,两者几乎一样  

### 类就像模块
你可以这样来理解模块,模块是一种专门的字典,能够储存 Python 代码,并用`操作符"."`来获取, Python 还有另一种结构,具有相似的功能,叫做`类`.类是可以将一组函数和数据放进容器,然后使用`"."`调用这些函数和数据.   

假设我们想创建一个类似` mystuff`模块的类,可以这样做:
```py
class Mystuff(object):
  def __init__(self):
    self.tangerine = "And now a thousand years between."
  def apple(self):
    print "I AM CLASSY APPLES!"
```
"类"看起来比"模块"要复杂,首先解决一个问题,为什么要用类代替模块:如果你愿意可同时调用上百万个类,并且不会相互冲突,但模块不行,模块只能被一个程序引用.除非你能破解 Python.  

在你能理解之前,你需要知道什么是"对象",它是怎么工作的.  

### 对象好似"迷你-imports"
如果把类比作"迷你模块",同样地可以把对象比作"迷你- imports",不过对于"类"来说,那个概念叫做"实例",当你创建一个类的实例,你就得到了一个"对象".  
```py
thing = Mystuff()
thing.apple()
print thing.tangerine
```
第一行是`实例`操作,有点像调用一个函数,然而当你调用的时候,Python 会为你启动一个事件顺序.我会用上边的代码来讲解这个流程:
1. Python 开始查找` Mystuff()` 发现这是一个你定义的类
2.
3. 接着 Python 看到你设置了一个魔术般的函数`__init__`,剩下的不知道怎么翻译了
4. 大概是说在函数中获取一个额外的变量` self`,是 Python 为用户设置的空的对象.我可以用它设置变量,就想使用模块,字典一样.
5. 在这个案例中,我为歌词设置了一个变量 `self.tangerine` ,然后将这个对象初始化.
6. 现在 Python 用这个刚制作的对象,分配给变量,以便用户使用

以上大致就是当你调用` class`时, Python 如何执行这个 `mini-import`.  

* 类就像关于创建新`mini-modules`的蓝图或者定义
* 实例就是关于你创建一个`mini-modules`的同时导入它
* 最终创建的这个` mini-modules`就叫做`对象`,然后你可以把它赋给变量去使用

## 三种获得内容的方式
```py
# dict style
mystuff['apples']

# module style
mystuff.apples()
print mystuff.tangerine

# class style
thing = Mystuff()
thing.apples()
print thing.tangerine
```
