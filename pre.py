import numpy as np
import pandas as pd
from csv import reader
import sklearn
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn import neighbors
from sklearn.preprocessing import Imputer
from dask.dataframe.io import csv

def load_data(filename,gradient,init_rate,maxrate):#梯度缺失率处理
    data = pd.read_csv(filename)
    print(data.shape)#矩阵形状
    print(data)
    
    (row_number,column_number) = data.shape#一行测序数据的数目

    init = init_rate
    droprate = np.zeros((10))
    for i in range(1,10):
        if droprate[i-1] <= maxrate:
            droprate[i-1] = init + gradient*i
        else:continue
    print(droprate)
    NA_data=data.replace(0,np.nan)#将0值转换为nan，方便后面调用函数
    print(NA_data)
    for i in range(1,10):
        if droprate[i-1] != 0 :
            deleted_data=NA_data.dropna(thresh=column_number*(droprate[i-1]))#依照缺失率删除缺失过多的序列
            #processed_data = deleted_data.apply(lambda x: (x - np.min(x)) / (np.max(x)-np.min(x)),axis=0)#归一化处理
            with open('preprocessed_data'+str(i)+'.csv','wb') as dataFile:
                deleted_data.to_csv('preprocessed_data'+str(i)+'.csv')
           
    
