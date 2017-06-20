### 练习49-形成句子
通过我们的游戏词典你应该可以看到如下列表:
```py
>>> from ex48 import lexicon
>>> print lexicon.scan("go north")
[('verb', 'go'), ('direction', 'north')]
>>> print lexicon.scan("kill the princess")
[('verb', 'kill'),('stop', 'the'), ('noun', 'princess')]
>>> print lexicon.scan("eat the bear")
[('verb', 'eat'),('stop', 'the'), ('noun', 'bear')]
.
.
.
```
现在我们为游戏添加些东西吧,比如`句型`,你还记得在高中时学的语法嘛?
> Subject Verb Object( 主动宾)

很明显这是最简单的句型,我们想做的是把上面列表中那些元组放进这种漂亮简单的句型中.
### 匹配和速览
要想实现它,我们需要4个工具:
1. 一种逐个检索列表中元组的方法.这很简单
2. 一种匹配不同类型元组使其能够装进 `主动宾`句型结构的方法
3. 一种快速浏览潜在可能元组的方法,能帮助我们做决断
4. 一种可以跳过无关紧要词汇的方法,比如` stop words`  

我们将会将这些函数放进一个名为` parser.py`的文件.我们先看一下第一个函数` peek`

 ```py
 def peek(word_list):
   if word_list:
     word = word_list[0]
     return word[0]
   else:
     return None
```
非常简单,接下来是` match`函数:
```py
def match(word_list, expecting):
  if word_list:
    word = word_list.pop(0)

    if word[0] == expecting:
      return word
    else:
      return None
  else:
    return None

```
还是很简单,对吧.最后是我们的` skip`函数
```py
def skip(word_list, word_type):
    while peek(word_list) == word_type:
      match(word_list, word_type)
```
现在你应该能够明白这些函数是干嘛的,一定确保你已经理解.   

### 句子的语法
借助我们的工具,我们可以从元组列表中的内容创建句型了.流程如下:  
1. 通过` peek`函数,识别下一个词汇.
2. 如果这个词汇匹配我们的语法,我们调用一个函数来处理它,这个函数是` parse_subject`
3. 如果不匹配,我们返回一个错误,也就是你这节练习要学的内容.
4. 当我们完成了所有事情后,我们的游戏还需要一个` sentence subject`.  

最好证明方法是我给你一段代码,但这节练习跟之前的不同之处在于,你需要自己为` parser code`编写代码. 下面是给你的代码.详情见`ex49.py`.  

### 词汇的例外情况
你已经详细学过`例外`,但是不知如何举出它们.这段代码将展示怎么做(在顶部` ParserError`部分). 注意我使用的是` class`处理例外.同样注意使用关键词来举出例外.  

在你的测试中,你需要亲自处理这些例外,我会告诉你如何做.  

### 你需要测试什么
在本练习中,编写一个完整的测试,确保每行代码都良好运行.将 test 放入` tests/parser_tests.py`,跟上一节练习类似.  

使用nose 文档中的` assert_raises`函数来检查例外情况.好好阅读 nose 的文档,学习如何使用这些函数,直到你可以自己编写测试文件.  

当你完成后,你应该了解一段代码是如何运行的,以及如何为它编写测试软件,并且能够为别人的代码编写测试.甚至在别人并没有要求你的情况下,相信我,这是一个非常实用的技能.  

### 课程训练
1. 修改` parse_methods`并试着将它放进` class`中而不是仅仅作一个 methods.你更喜欢哪种设计呢?
2. 让你的` parser`具备更强的纠错性能.那么当你用户键入词典之外的词汇时,体验就不会那么差了.  
3. 改善语法,使其能处理更多内容,比如数字
4. 思考一下如何发挥` sentence class`的作用,让用户输入能变得更有趣.
