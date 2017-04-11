## 练习30-Else 和 If
上一节练习中你写了一些`if 语句( if-statement)`,并且试图了解他们是什么,以及实现的是什么功能.在你继续学习之前,我给你解释一下,上一节*课程训练*的答案.
1. 你认为` if`对于它的下一行代码做了什么? if语句为代码创建了一个所谓的`分支`,if 语句告诉你脚本:"如果这个布尔表达式为真,就运行接下来的代码,否则就跳过."
2. 为什么 if 语句的下一行需要4个空格的缩进?行尾的冒号的作用是告诉 Python 接下来你要创建一个新的代码区块.这创建函数时结尾加冒号是一个道理.
3. 如果不缩进,会发生什么事情?如果没有缩进,你应该会看到 Python 报错, Python 的规则里,只有一行以`:`结尾,它接下来的内容就应该有缩进.
4. 把练习26中的其他布尔表达式放到 if 语句中是否也可以运行?  可以.而且不管多复杂都可以,虽然写负责的东西通常是一种不好的编程风格.
5. 如果把变量` people`,`cats`,和`dogs`的初始值改掉,会发生什么事情?因为你比较的对象是数字,如果你把这些数字改掉的话,某些位置的 if 语句会被演绎为` True`,而它下面的代码区块将会被运行.你可以试着修改,然后再脑海里推演一下那段代码会被运行.

### 课程训练
1. 猜想一下,`elif`和` else`的功能.
2. 将`cars`,`people`,和` buses`的数量改掉,然后追溯每一个 if 语句.看看最后会打印出什么来
3. 试着写一些复杂的布尔表达式,例如 `cars > people and buses < cars`
4. 在每一行写上注释,说明这一行的作用