## 1.语法错误
提示:
```
Traceback (most recent call last):
  File "ex20.py", line 33, in <module>
    print_a_line(current_line,current_file)
TypeError: 'tuple' object is not callable
```
原因:
```
current_line = 1 + current_line
print_a_line(current_line, current_file)
```
在`current_line`和`current_file`之间的`,` 是中文输入法.改成英文输入法就好了.真是超级难排查.
