# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 11:43:55 2018

@author: Administrator
合并所有excel
"""

import pandas,numpy
import matplotlib.pyplot as plt
import pandas as pd
import os

#读取所有文件
file_List=os.listdir("statistics_save/") 
#最终表格，存储有价值变量
df_all_valueableVariable=pd.DataFrame()
for file in file_List:
    print(file)
    df=pd.read_excel("statistics_save/"+file)
    #横向连接两个变量字段
    df_all_valueableVariable=pd.concat([df_all_valueableVariable,df],axis=0)

df_all_valueableVariable.to_excel("所有市场调整后价格.xlsx")
