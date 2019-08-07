#AutoTraceDraw.py
#根据数据接口的信息画图像
import turtle as t
t.title('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
#数据读取
detals=[]
f=open("data.txt")
for line in f:
    line =line.replace("\n","")  
    detals.append(list(map(eval,line.split(","))))#map()函数，将函数类型的参数1作用于每一个序列类型的参数2
f.close()
#自动控制 第0个数据：前进的距离；1：是否转向：2：向右转为1向左转为0；345：RGB颜色数值
for i in range(len(detals)):
    t.pencolor(detals[i][3],detals[i][4],detals[i][5])
    t.fd(detals[i][0])
    if detals[i][1]:
        t.right(detals[i][2])
    else:
        t.left(detals[i][2])
