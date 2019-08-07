#Daydayup.py
def Daydayup(Dayrate):
    Dayup =1.0
    for i in range(52):
        for t in range(5):
            Dayup =Dayup *(1+float(Dayrate))
        for t in range(2):
            Dayup*=(1-0.01)
    Dayup*=(1+float(Dayrate))
    return Dayup
Rate=0.01
while Daydayup(Rate)<37.78:
    Rate+=0.001
print("工作努力的参数是：{:.3f}".format(Rate))
 
