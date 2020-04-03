"""
第一个python代码

引入 turtle库的几种方式
第一种：
import turtle

turtle.pensize(4)
turtle.pencolor('red')

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.circle(200)
turtle.mainloop()

第二种
from turtle import *

pensize(4)
pencolor('red')

forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
circle(200)
mainloop()

第三种
import turtle as t

t.pensize(4)
t.pencolor('red')

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.circle(50)
t.right(90)
t.forward(100)
t.right(90)
t.circle(50)
t.mainloop()

"""

"""
绘制国旗
"""
import turtle as t


def draw_rectangle(x, y, width, height):
    """绘制矩形"""
    t.goto(x, y)
    t.pencolor('red')
    t.fillcolor('red')
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def draw_star(x, y, radius):
    """绘制五角星"""
    t.setpos(x, y)
    pos1 = t.pos()
    t.circle(-radius, 72)
    pos2 = t.pos()
    t.circle(-radius, 72)
    pos3 = t.pos()
    t.circle(-radius, 72)
    pos4 = t.pos()
    t.circle(-radius, 72)
    pos5 = t.pos()
    t.color('yellow', 'yellow')
    t.begin_fill()
    t.goto(pos3)
    t.goto(pos1)
    t.goto(pos4)
    t.goto(pos2)
    t.goto(pos5)
    t.end_fill()


def main():
    """主程序"""
    t.speed(12)
    t.penup()
    x, y = -270, -180
    """画国旗主体"""
    width, height = 540, 360
    draw_rectangle(x, y, width, height)
    """画大星星"""
    pice = 22
    center_x, center_y = x + 5 * pice, y + height - pice * 5
    t.goto(center_x, center_y)
    t.left(90)
    t.forward(pice * 3)
    t.right(90)
    draw_star(t.xcor(), t.ycor(), pice * 3)
    x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]
    """画小星星"""
    for x_pos, y_pos in zip(x_poses, y_poses):
        t.goto(x + x_pos * pice, y + height - y_pos * pice)
        t.left(t.towards(center_x, center_y) - t.heading())
        t.forward(pice)
        t.right(90)
        draw_star(t.xcor(), t.ycor(), pice)
    # 隐藏海归
    t.ht()
    # 显示绘图窗口
    t.mainloop()


if __name__ == '__main__':
    main()
