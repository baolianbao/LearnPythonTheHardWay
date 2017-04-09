## 练习32-循环和列表
你现在应该可以开发一些有意思的小程序了.如果你继续学习,你会意识到你可以把所有你学过东西组合起来运用,再结合 `if-statement`和`布尔表达式`,能使程序做很多有智能的东西.  
然而,程序也需要快速重复性的事务,我们在本节练习中将要使用` for-loop(for 循环)`去创建和显示变量列表.当你做这些练习时,你将会理解它们是什么? 我不会立刻告诉你,你需要自己思考答案.  
在你能使用 for-loop 之前,你需要掌握将`loop`的结果存储在某个地方的方法.答案是最好用一个`list`,`list`的作用和其名字差不多:它是一个容器,将内容有序整理.这并不复杂,你只需要学习一个新语法,下面示范如何创建一个` list`:
```py
  hairs = ['brown','blond','red']
  eyes = ['brown','blue','green']
  weights = [1, 2, 3, 4]
```
上面是三个` list`,很简单,你可看到它们都以`[`开始,然后将项目挨个填充进去,用`,`隔开,就像函数参数一样.最后用`]`告诉 Python 这是结尾.最好 Python 将个列表和其中的内容赋给变量.  
  > **注意**,这是一个新手容易迷惑的地方,常识教导我们这个世界是平的,但大部分人没有考虑过什么是`嵌套结构`,但这在程序中是最常见的.这有个建议,如果你某个地方不懂,拿出纸和笔,手工把代码抄下来然一个比特,一个比特地研究,直到弄懂为止.

### 课程训练
1. 看一下你是怎么使用` range`的,上网搜索它是干嘛的,弄懂.
> range(start, stop, [step]) 这是个多功能函数,用来创建算数级别的列表,在 `for`循环中非常常用,参数必须是整数,`step`是省略的参数,默认是 1 ,`start`参数也可以省略,默认是 0 ,  例如:
```py
 range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 range(0, 30, 5)
[0, 5, 10, 15, 20, 25]
range(1, 0)
[]
range(0, -10, -1)
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
```
2. 你是否在代码第22行,完全没有使用` for-loop`,只是将 `range`,直接赋予` elements`?
3. 查阅 Python 官方帮助文档中关于 `lists`的内容,看看除了`append`,还可以做哪些方法.
>  list.count(obj) -- 统计元素 obj 在 list 中出现的次数.  
> Example:
 ```py
aList = [123, 'xyz', 'zara', 'abc', 123];
print "Count for 123 : ", aList.count(123)
Count for 123 :  2
```
> list.extend(seq) -- 将 seq 中的元素添加到 list 中  
> Example:
```py
aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)
print "Extended List : ", aList
Extended List :  [123, 'xyz', 'zara', 'abc', 123, 2009, 'manni']
```
> list.index(obj) -- 返回 obj 在 list 中的索引位置  
> Example:
```py
aList = [123, 'xyz', 'zara', 'abc'];
print "Index for xyz : ", aList.index( 'xyz' )
Index for xyz :  1
```
> 还有 list.insert(index, obj) --在制定位置插入 obj.  
> list.pop(obj=list(-1)) -- 从最后一个位置开始移除 obj,  
> list.remove(obj) -- 将 obj 从 list 中移除  
> list.reverse() -- 倒序排列所有元素  
> list.sort([func]) -- 整理 list 中的元素顺序
