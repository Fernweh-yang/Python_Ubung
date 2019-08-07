#PythonDraw.py
import turtle
#turtle.setup(width,height,startx,starty)
turtle.setup(650,350,200,200)
#turtle.penup()画笔抬起，让海龟飞起，此时移动海龟不在屏幕上落下任何痕迹。
turtle.penup()
#turtle.fd(d)让海龟走直线，d是行进距离（像素））
turtle.fd(-250)
#turtle.pendown()画笔落下，让海龟落下
turtle.pendown()
#turtle.pensize()画笔的宽度，即海龟腰围
turtle.pensize(25)
#turtle.pencolor(0.63，0.13，0.94) 可以是颜色字符串也可以是R,G,B值
turtle.pencolor("purple")
#turtle.seth(angle)  改变海龟前进方向为确定的一个角度
#turtle.left(angle)  海龟向左转某一角度
#turtle.right(angle) 海龟向右转某一角度
turtle.seth(-40)
#range(N)产生0到N-1的整数序列
#range(M,N)产生M到N-1的整数序列
for i in range(4):
    #turtle.circle(r,extent)根据半径r绘制extent角度的弧形；
    #r：默认圆心在海龟左侧r距离的位置.若为负值，则圆心变到右侧
    #extent:走过角度，默认为360
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
#turtle.done()使程序不会自动退出，需要手动退出
turtle.done()
