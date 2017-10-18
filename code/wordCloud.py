# -*- coding: utf-8 -*-
import sys
import jieba
import numpy as np
from PIL import Image
import pickle
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator



# 直接从文件读取数据，文件中存放的是要生成词云的文件，如19da.txt为19大工作报告
wordcloudsfile = "C:/Users/Administrator/Desktop/mytest/19da.txt"
#此处是要添加的词云分析时用到的词典，这个词典越全越好
userDic = "E:/历史数据/dic.txt"
#此处的wordCnt.txt为统计词频后的文件存放位置，写好即可
wordCntpth = "E:/test/wordCnt.txt"
text = open(wordcloudsfile,'rb').read()
jieba.load_userdict(userDic)
word_jieba = jieba.cut(text)
word_split = " ".join(word_jieba)
word_lst = []
word_dict= {}
#统计词频
for word in word_split:
    word_lst.append(str(word).split(','))
    for item in word_lst:
        for item2 in item:
            if item2 not in word_dict:
                word_dict[item2] = 1
            else:
                word_dict[item2] += 1
with open(userDic,'w') as wf2:#此处的wordCnt.txt为统计词频后的文件存放位置，写好即可
    for key in word_dict:
        wf2.write(key + ' ' + str(word_dict[key]) + '\n')
#设置生成词云的背景图片,此处可以随意选一张自己喜欢的图片的绝对路径
backgroud_Image = plt.imread(r'D:\PyCharm\Python3.6\Lib\site-packages\wordcloud\222.jpg')
wc = WordCloud( background_color = 'white',
                mask = backgroud_Image,
                width=1000,
                height=1000,
                max_words = 500,
                stopwords = STOPWORDS,
                font_path = r'D:\PyCharm\Python3.6\Lib\site-packages\wordcloud\simhei.ttf',#设置字体，如不设置，则会无法解析中文
                max_font_size = 100,  # 字体最大值
                random_state = 400
)
wc.generate(word_split)
image_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func = image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()
