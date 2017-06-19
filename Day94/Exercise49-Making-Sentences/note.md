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
