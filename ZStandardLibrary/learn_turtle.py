"""
Learn turtle
https://docs.python.org/3/library/turtle.html?highlight=turtle#module-turtle

在1966年，Seymour Papert和Wally Feurzig发明了一种专门给儿童学习编程的语言——LOGO语言，
    它的特色就是通过编程指挥一个小海龟（turtle）在屏幕上绘图。
海龟绘图（Turtle Graphics）后来被移植到各种高级语言中，
    Python内置了turtle库，基本上100%复制了原始的Turtle Graphics的所有功能
"""

from turtle import *

# width(4)
#
# # 前进:
# forward(200)
# # 右转90度:
# right(90)
#
# # 笔刷颜色:
# pencolor("red")
# forward(100)
# right(90)
#
# pencolor("green")
# forward(200)
# right(90)
#
# pencolor("blue")
# forward(100)
# right(90)
#
# # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
# done()

# 使用递归，可以绘制出非常复杂的图形 (分型树)
# 设置色彩模式是RGB:
colormode(255)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)

speed("fastest")

draw_tree(l, 4)

done()
