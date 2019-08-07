#CalPi.py
#蒙特卡罗法求解
import random
import time
DARTS=1000*1000     #投点数
hits=0.0            #在=落在圆内的数
start=time.perf_counter()
for i in range(1,DARTS+1):
    x,y=random.random(),random.random()
    dist=pow(x**2+y**2,0.5)
    if dist <=1.0:
        hits=hits+1
pi =4*(hits/DARTS)
print("圆周率是:{}".format(pi))
end=time.perf_counter()
long=end-start
print("运行时间是:{:.5f}s".format(long))
