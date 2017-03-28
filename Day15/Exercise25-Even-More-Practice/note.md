## 练习25-更多的练习
我们将要做一些练习包括函数和变量,确保你非常了解他们. 这节练习的代码你应该直接了当地敲出,分解,并理解.  
然而,这节练习有一点不同.你不需要运行它.取而代之的是你应该导入到 python,自己通过函数来运行它.

### 课程训练
1. 搞清楚你写的模块,以及里面的每个函数是干嘛的.
2. 试着输入`help(ex25)`或者` help(ex25.break_words)`.你会看到,模块的帮助信息就是你在每个函数里`"""`的内容.它叫`注释文档`,很多时候我们就是靠它学习编程语言的.
3. 直接输入`ex25.`是很烦人的,因为它等于` from ex25 import *`,意思从模块` ex25`中导入所有东西.程序喜欢倒序理解.
4. 分解你的代码文件,通过 python 解释器来执行看会是什么样子.
```
>>> import ex25
>>> txt = open(raw_input("filename:"))
filename:ex25.py
>>> sorted_words = txt.read()
>>> sorted_words
'def break_words(stuff):\n    """This function will break up words for us."""\n    words = stuff.split(\' \')\n    return words\n\ndef sort_words(words):\n    """Sorts the words."""\n    return sorted(words)\n\ndef print_first_word(words):\n    """Prints the first word after popping it off."""\n    word = words.pop(0)\n    print word\n\ndef print_last_word(words):\n    """Prints the last word after popping it off."""\n    word = words.pop(-1)\n    print word\n\ndef sort_sentence(sentence):\n    """Take in a full sentence and returns the sorted words."""\n    words = break_words(sentence)\n    return sort_words(words)\n\ndef print_first_and_last(sentence):\n    """Prints the first and last words of the sentence."""\n    words = break_words(sentence)\n    print_first_word(words)\n    print_last_word(words)\n\ndef print_first_and_last_sorted(sentence):\n    """Sorts the words then prints the first and last one."""\n    words = sort_sentence(sentence)\n    print_first_word(words)\n    print_last_word(words)\n'
>>>
```
就是这个样子.你可以用 Ctrl + D 来关闭解释器.
