## 练习39-字典,可爱的字典
 接下来,我要介绍一个重量级的数据容器,可能会让你有点头疼,因为一个超酷的宏伟的世界向你扑面而来.这绝对是最有用的容器:**字典**.  
 在 Python 中称为`dicts`,其他编程语言叫它` hashes`.我倾向于两者都用.但这不是重点.重点是字典与列表的差别.你可以用列表做这类事:
 ```
>>> things = ['a', 'b', 'c', 'd']
>>> print things[1]
    b
>>> things[1] = 'z'
>>> print things[1]
    z
>>> print things
    ['a', 'z', 'c', 'd']

```
你可以用数字作为列表的索引.也即你可以通过数字找到列表中的元素.而 `dict`不同,它可以让你通过任何东西找到元素.不只是数字.是的,字典可以就; 一个元素和另一个关联,不管他们的类型是什么,我们来看:
```
>>> stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
>>> print stuff['name']
Zed
>>> print stuff['age']
36
>>> print stuff['height']
74
>>> stuff['city'] = "San Francisco"
>>> print stuff['city']
San Francisco
```
如上所示,我们除了用数字,还可以用字符串来中字典中获取内容.同时还可以用字符串来往字典中添加元素.当然它支持的不只有字符串,我们还可以做这样的事:
```
>>> stuff[1] = "Wow"
>>> stuff[2] = "Neato"
>>> print stuff[1]
Wow
>>> print stuff[2]
Neato
>>> print stuff
{'city': 'San Francisco', 2: 'Neato',
'name': 'Zed', 1: 'Wow', 'age': 36,
'height': 74}
```
除了往字典里添加东西,还可以从字典里往外删除东西.即使用` del`:
```
>>> del stuff['city']
>>> del stuff[1]
>>> del stuff[2]
>>> stuff
{'name': 'Zed', 'age': 36, 'height': 74}
```

### 课程训练
1. 在 python 文档中找到关于 dictionary(或者 dicts, dict) 的内容,学着对 dict 做更多的操作.
2. 找出一些 dict 无法做到的事情,例如比较重要的一个内容是, dict 的内容是无序的,你可以试试看是否如此
3. 试着把 for-loop 执行到 dict 上面,然后试着在 for-loop 中使用 dict 的 items()函数,看看会有什么样的结果.
