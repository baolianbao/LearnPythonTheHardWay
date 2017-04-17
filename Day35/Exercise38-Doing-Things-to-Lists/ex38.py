# -*- coding: utf-8 -*-
ten_things = "Apples Oranges Crow Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:     # 这个循环的作用是为 stuff 添加元素,直到元素个数达到10个为止
    next_one = more_stuff.pop() #取出 more_stuff的最后一个元素,赋予 next_one
    print "Adding: ", next_one # 打印 next_one中的内容
    stuff.append(next_one)#将 next_one 中的内容添加到 stuff 尾部
    print "There's %d items now." % len(stuff) #显示这是第几个项目

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]#显示第二个元素
print stuff[-1]#显示倒数第一个元素
print stuff.pop()#取出并显示倒数第一个元素
print ' '.join(stuff) #what? cool! 为元素之间添加空格,
print '#'.join(stuff[3:5])#super stellar
