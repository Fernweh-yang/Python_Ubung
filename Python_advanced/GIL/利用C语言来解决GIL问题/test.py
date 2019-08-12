from ctypes import *
from threading import Thread

#加载动态库
lib = cdll.LoadLibrary("./library.so")

#创建一个子线程，让其执行c语言编写的程序，此函数是一个死循环
t = Thread(target=lib.DeadLoop)
t.start()

#主程序
while True:
    pass
