import wordcloud
import jieba 
txt="我不相信天赋，我站在这里是因为努力，无论你想达成什么目标，记得去努力"
w= wordcloud.WordCloud( width=1000,font_path="msyh.ttc",height=700)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("pywcloud.png")
