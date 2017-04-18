## 练习39 列表的操作
你已经学过了列表,在你学习`while循环`的时候,你对列表进行过`追加( append)`操作,而且将列表的内容打印了出来.另外你应该还在课程训练中研究过 python 的文档,看了列表支持的其他操作.如果你忘记了,就回到前面复习一下.  

当你看到像 `mystuff.append('hello')`这样的代码时,你实际已经在 Python 内部激发了一个连锁反应.以下是它的工作原理:
1. Python看到你用了 `mystuff`,就开始去找这个变量.也许它需要倒着检查哪里用 `=` 创建过这个全局变量,或者检查它是不是一个全局变量.不管哪种方式它得先找到`mystuff`这个变量才行.
2. 一旦找到了` mystuff`,就轮到处理`. (句号)`这个操作符,而且开始查看`mystuff`
内部的一些变量了.由于` mystuff`是一个列表, Python 知道 `mystuff`支持一些参数.
3. 接下来轮到处理` append`,Python 会将`append`和 `mystuff`所支持的函数一一对比,如果确实有一个叫做 `append`的函数,那么 Python 就会使用这个函数.
4. 接下来 Python 看到了括号`()`,并且意识到,这应该是一个函数.到这个步骤,它就会正常调用这个函数.不过这个函数还需要多一个参数才行.
5. 这个额外的参数,其实是...` mystuff`,我知道,这很奇怪,不过这就是 Python 的工作原理,所以还是记住这一点,就当它是正常的好了.真正的写法应该是` append(mystuff, 'hello')`,不过你看到的只是 `mystuff.append('hello')`.

大部分时候你不需要知道这些细节,如果你看到想这样的报错,上面这些细节就对你有用了:
```
$ python
Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41)
[GCC 4.4.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
 >>> class Thing(object):
...  def test(hi):
...         print "hi"
...
>>> a = Thing()
>>> a.test("hello")
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: test() takes exactly 1 argument (2 given) >>>
```
上述代码中的` class`你还没学到,不过后面很快就要碰到了.现在你看到 Python 说`test() takes exactly 1 argument (2 given)`,只可以接受1个参数,实际上给了2个. 它意味者 Python 把` a.test("hello")`改成了 `test(a,"hello")`.声明 **test** 这个函数时.没有为它添加 **a** 这个参数.

## 课程训练
1. 将每一个被调用的函数以上述方式翻译成 Python 实际执行的动作.例如:`' '.join(things)`其实是 `join(' ',things).`
2. 将这两种方式翻译为自然语言.例如,`' '.join(things)`可以翻译成"用空格连接(join)things",而 join(' ',things)的意思是"为 ' '和 things"调用join函数,这其实是同一件事情.
3. 上网阅读一些关于"面向对象编程( Object Oriented Programming)"的资料,别担心,在本书中你将从本书中学到足够用的关于面向对象编程的基础知识,而以后你还可以慢慢学到更多.
4. 查一下 Python中的` class`是什么东西.不要阅读其他语言的` class`用法,会把你搞糊涂
5. dir(something)和 something 的 class 有什么关系
6. 如果你觉得 面向对象编程太难了,你可以开始学一下"函数编程(functional Programming)"
