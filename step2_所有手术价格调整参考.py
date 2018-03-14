# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 10:18:04 2018
@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import normality_check
from scipy.stats import mode
#读取单个文件
#FileName="眼部_双眼皮_切开.xlsx"
#读取所有文件
file_List=os.listdir("save/") 
#创建新的统计后文件，statistics_save文件
newFile=os.mkdir("statistics_save/") 

def calculate_single(FileName):
    #读取excel
    df=pd.read_excel("save/"+FileName)
    申请金额=df['申请金额']
    series_子类标准价格=df['子类标准价格']
    #手术名
    手术名=df['手术名'].values[0]
    描述性统计=申请金额.describe()
    样本量=描述性统计[0]
    子类标准价格=series_子类标准价格.values[0]
    最小值=申请金额.min()
    最大值=申请金额.max()
    平均数=申请金额.mean()
    中位数=申请金额.median()
    #众数=float(申请金额.mode())
    众数=mode(申请金额).mode[0]
    四分之一位数=描述性统计[4]
    四分之三位数=描述性统计[6]
    标准差=描述性统计[2]
    IQR=四分之三位数-四分之一位数
    #异常值上线upper inner fence,异常值下限lower inner fence
    异常值上线=四分之三位数+1.5*IQR
    异常值下线=四分之一位数-1.5*IQR
    upper_outer_fence=四分之三位数+3*IQR
    lower_outer_fence=四分之一位数-3*IQR
    if 样本量>3:
        正态性=normality_check.check_normality(申请金额)
    else:
        正态性=False
    if 异常值下线<最小值:
        异常值下线=最小值
    if lower_outer_fence<0:
        lower_outer_fence=0
     
    参考价格=中位数
    #避免两端极值和商户活动降价影响
    参考区间=(四分之一位数,四分之三位数)
    market_price_range=(异常值下线,异常值上线) 
    #极端异常值：小于lower_outer_fence或大于upper_outer_fence
    extreme_outlier=(lower_outer_fence,upper_outer_fence)
    list_名称=["手术名","样本量","子类标准价格","最小值","最大值","平均数","中位数","众数","四分之一位数","四分之三位数","IQR","异常值上线","异常值下线","标准差","正态性","参考价格","参考区间","价格正常区间","（区间外）极端异常值"]
    list_value=[手术名,样本量,子类标准价格,最小值,最大值,平均数,中位数,众数,四分之一位数,四分之三位数,IQR,异常值上线,异常值下线,标准差,正态性,参考价格,参考区间,market_price_range,extreme_outlier]
    df_save=pd.DataFrame(data=[list_value],index=[0],columns=list_名称)
    df_save.to_excel("statistics_save/"+手术名+"市场参考价格.xlsx")

def calculate_all(file_List):
    for excel in file_List:
        print(excel)
        calculate_single(excel)

calculate_all(file_List)