#WeekStr
'''WeekStr="星期一星期二星期三星期四星期五星期六星期天"
WeekId=eval(input("请输入星期几"))
print(WeekStr[(WeekId-1)*3:(WeekId-1)*3+3])'''
WeekStr="一二三四五六七"
WeekId=eval(input("请输入星期1-7的一个数"))
print("星期"+WeekStr[WeekId-1])
