#CalBMI.py
height,weight=eval(input("请输入身高（米）和体重（公斤）[并用逗号隔开]："))
bmi=weight/pow(height,2)
print("BMI的数值为{:.2f}".format(bmi))
nei,wai ="",""
if bmi<18.5:
    nei,wai="偏瘦","偏瘦"
elif 18.5<=bmi<24:
    nei,wai="正常","正常"
elif 24<=bmi<25:
    nei,wai="偏胖","正常"
elif 25<=bmi<28:
    nei,wai="偏胖","偏胖"
elif 28<=bmi<30:
    nei,wai="肥胖","偏胖"
elif 30<=bmi:
    nei,wai="肥胖","肥胖"
print("在国内属于{}，在国外属于{}".format(nei,wai))
