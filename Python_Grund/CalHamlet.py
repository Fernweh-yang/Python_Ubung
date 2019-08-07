#CalHamlet.py
def getText():          
    txt=open(r'C:\Users\Fernweh\Desktop\Hamlet.txt',"r").read()
    txt=txt.lower()         #将所有英文字符变为小写
    for ch in '|#$%&()*+_,<>.?[]\/!@=~:"\'':    #将所有特殊字符去除变为空格
        txt=txt.replace(ch," ")
    return txt
hamleTxt = getText()
words = hamleTxt.split()    #将字符串变为一个个字符串文字
counts={}
for word in words:          #将每个单词和其出现的次数用字典类型将其映射
    counts[word]=counts.get(word,0)+1
items=list(counts.items())  #将字典类型转换为列表类型
items.sort(key=lambda  x:x[1],reverse=True)  #用sort方法，来对其排序
for i in range(1000):         #选出出现次数最高的10个单子
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))
    
