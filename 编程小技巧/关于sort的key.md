- 一个二维列表：想让他先按第一个元素从大到小排列，如果一样大就第二个元素小的在前面  
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]  
就可以活用key参数：
```
people=sorted(people, key=lambda x:(-x[0],x[1]))
new_people = list()      //列表要先定义一下
for i in people[0:]:     //遍历从哪到哪的控制
    new_people.insert(i[1],i)   //插入要告诉插入的位置
```
