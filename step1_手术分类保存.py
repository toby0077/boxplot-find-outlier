# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 09:17:02 2018

@author: Administrator
市场价格调整
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#读取文件
readFileName="data.xlsx"
#创建save文件
newFile=os.mkdir("save/") 

#读取excel
df=pd.read_excel(readFileName)
series_手术名=df["手术名"].dropna()
#手术频率统计
手术统计=series_手术名.value_counts()
'''
眼部_双眼皮_切开                   776
注射类_玻尿酸_进口                  679
鼻部_鼻综合_鼻综合                  648
。。。。
'''
#所有手术种类，存放在列表内
list_手术类型=list(手术统计.index)
'''
['眼部_双眼皮_切开', '注射类_玻尿酸_进口,,,,,]'
'''
#统计数量
手术数量=手术统计.size
'''
Out[14]: 88
'''

for name in list_手术类型:
    df_name=df[df.手术名==name]
    #保存数据
    df_name.to_excel("save/"+name+".xlsx", sheet_name='Sheet1')
