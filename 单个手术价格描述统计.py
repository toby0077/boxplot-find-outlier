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
#读取文件
FileName="注射类_玻尿酸_国产.xlsx"
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
众数=mode(申请金额).mode[0]
四分之一位数=描述性统计[4]
四分之三位数=描述性统计[6]
标准差=描述性统计[2]
IQR=四分之三位数-四分之一位数
异常值上线=四分之三位数+1.5*IQR
异常值下线=四分之一位数-1.5*IQR
upper_outer_fence=四分之三位数+3*IQR
lower_outer_fence=四分之一位数-3*IQR
if lower_outer_fence<0:
        lower_outer_fence=0
#避免两端极值和商户活动降价影响
参考区间=(四分之一位数,四分之三位数)
if 样本量>3:
    正态性=normality_check.check_normality(申请金额)
else:
    正态性=False
参考价格=中位数
market_price_range=(异常值下线,异常值上线)  

#绘制正太分布图
申请金额.hist()
df1=pd.DataFrame(申请金额)
fig,ax=plt.subplots()
a=df1.boxplot(ax=ax)
plt.savefig('pig.png')

def 异常值判断(数字):
    if 数字>异常值上线 or 数字<异常值下线:
        print("%f 是异常值"%数字)
        return True
    else:
        print("%f 不是异常值"%数字)
        return False
 
#箱型图市场价格取值范围
def Boxer_Market_price_range(异常值下线,异常值上线):
    if 异常值下线<最小值:
        异常值下线=最小值
    return (异常值下线,异常值上线)

#正态分布市场价格取值范围
market_price_range=Boxer_Market_price_range(异常值下线,异常值上线)
extreme_outlier=(lower_outer_fence,upper_outer_fence)
print(手术名)
print("参考价格:",参考价格)
print("参考区间:",参考区间) 
print("价格正常区间:",market_price_range)
print("超出此范围的是价格极端异常值区间:",extreme_outlier)
print("描述性统计:",描述性统计)
#测试1.5万是否属于正常市场价格
#异常值判断(15000)

#名称列表
list_名称=["手术名","样本量","子类标准价格","最小值","最大值","平均数","中位数","众数","四分之一位数","四分之三位数","IQR","异常值上线","异常值下线","标准差","正态性","参考价格","参考区间","市场价格正常区间","（区间外）极端异常值"]
list_value=[手术名,样本量,子类标准价格,最小值,最大值,平均数,中位数,众数,四分之一位数,四分之三位数,IQR,异常值上线,异常值下线,标准差,正态性,参考价格,参考区间,market_price_range,extreme_outlier]
df_save=pd.DataFrame(data=[list_value],index=[0],columns=list_名称)
df_save.to_excel(手术名+"市场参考价格.xlsx")

