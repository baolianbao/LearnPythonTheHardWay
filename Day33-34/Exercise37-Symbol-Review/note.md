#练习37-复习 符号
现在该复习你学过的 Python 关键字了,而且在本节中你还会学习到一些新的东西,我在本节将所有 python 符号和关键字列出来,这些都是值得掌握的重点.  
在这节课中,你需要复习每一个关键字,先写下你的印象,然后去网上查找准确定义,进行对比.如果你的印象是不准确的,就写下它的真正定义,反复记牢.  
最后,将这些关键字用起来,也就是将它们写到程序里,你可以是一个程序,也可以用多个程序来实现.通过这种方式来巩固自己的记忆.

**关键字** | 印象 | 定义
-------------|-----|-----
and| 布尔运算符号,做[与运算],左右两边需要2个参数,同时为True 则返回 True, 否则返回 False| 所有的布尔表达式条件必须被满足即为真
del| 没有用过,不知道|删除对象
from|调用 Python 内置模块时使用|从模块中导入一个特定的变量,类,或者函数
not| 布尔运算符号,做[非运算],右边有一个参数|否定一个布尔值
while| 无限循环代码块,直到结果返回为 False|控制程序的流程
as| 没印象|给模块起一个别名
elif| if 语句的扩展选项,当条件为True 执行代码|可以替代 if, 当第一个测试为 False 时,运行下一个
global| 应该声明全局变量使用的 |访问函数外部的全局变量
or| 布尔运算符号,做[或运算],需要2个参数,只有其中一个为 True, 就返回 True.|至少有一个表达式被满足
with| 没有用过|
assert|没有用过|
else|if 语句的组成部分,每个 if 语句必须包含一个 else, 当 if 条件为 False 时,执行 else 的代码.|是可选的,跟我的印象一致
if|条件判断语句,结构是 `if + 条件 + : + else`,if 语句可以包含 if 语句,但最好不要超过2层,如果条件为True 就执行 if 下的代码,如果为 False就执行 else 下的代码.|用来决断哪条命令被执行
pass|没用过|什么都不做
yield|没用过|用来配合生成器使用
break|没印象|中断循环
except|没有用过|获取例外并执行代码
import| 导入 Python 内置函数的方法|从外部导入模块到脚本
print| 将后边的内容输出到屏幕上,最最常用的一条命令|打印到控制台
class| 应该是分类什么的.|创建自定义对象
exec| 执行代码|动态执行 Python 代码
in| for 循环中使用的命令,用来从 list 中提取元素.|
raise| 没有用过|创建自定义例外
continue| 没有用过|中断当前循环,但并不跳出整个循环,而是开始一个新的循环
finally| 没有用过|总是在最后一步执行,用来清空资源
is| 没有用过|测试对象的标识
return| 函数中会使用这个命令,用来返回一些值|退出函数,并返回一个变量值
def| 每个函数前边都需要 加 def |创建用户自定义函数
for|for 循环,一般配合list 使用,执行一些重复操作,相当好用.|遍历集合中的每一个项目
lambda| 没有用过|创建一个匿名函数
try| 没有用过|制定例外操作者


**数据类型** | 印象 | 定义
------------|-----|
True |真值|布尔值的一种
False |非真值|布尔值的一种
None | 无|
strings |字符串|储存文本,比如字母,文字,符号,控制符号等多达20亿种字符
numbers |数值|
floats |浮点数,用来表示小数|
lists |列表|

**转义字符序列** | 印象 | 定义
---------------|------|----
\\ | 在打印结果中正常显示`\`|表示`\`
\' | 在结果中显示`'`|表示`'`
\" |在结果中显示'"'|表示`"`
\a |没印象|让设备发出警告
\b |没印象|删除键
\f |没印象|跳页
\n |换行符|换行符
\r |没印象|回车
\t |没印象|作用类似 tab 键
\v |没印象|垂直制表符

**格式字符串** | 印象 | 定义
-------------| -----|-----
%d |大部分都没印象,不太知道它们是干嘛的|十进制整数
%i |同上|类似% d
%o |同上|八进制数字
%u |同上|无符号十进制数字
%x |同上|小写十六进制
%X |同上|大写十六进制
%e |同上|小写指数符号
%E |同上|大写指数符号
%f |同上|浮点实数
%F |同上|类似于% f
%g |同上|在浮点实数和十六进制中任选一个最短的表达方法
%G |同上|类似% g, 但是要大写
%c |同上|字符格式
%r |不管是什么类型,都输出|调试字符格式
%s |同上|字符串格式
%% |同上|百分比符号


**操作符** | 印象| 定义
--------| ----|-----
+ |等于数学的加号|加法
- |等于数学的减号|减法
* |等于数学的乘号|乘号
** |没用过|
/ |等于数学的除号|除号
// |不知道|
% |取余运算|
< |比大小|小于
> |比大小|大于
<= |比大小|小于等于
>= |比大小|大于等于
== |比较两边的变量是否相等,等同` and`|等号
!= |作用等同 `not`|不等于
<> |作用还不知道|
()|用于函数的参数|
[] |不知道 |
{} |标记代码|
@ |没用过|
, |用来分割变量 和参数等|
: |声明变量和函数时必须以它结尾|