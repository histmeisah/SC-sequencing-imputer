import csv
import pandas as pd
import numpy as np
import cloudpickle
from sklearn.preprocessing import Imputer
from csv import reader
import os
import impyute
from impyute.imputation.cs import buck_iterative
import fancyimpute
from fancyimpute import IterativeSVD, KNN, MatrixFactorization, NuclearNormMinimization,BiScaler
import time
from sklearn.impute._iterative import IterativeImputer



def mean_impute(data,result):#均值填补
    
    dataframe=pd.read_csv(data)
    imp = Imputer(missing_values='NaN',strategy='mean',axis=0)
    imp.fit(dataframe)
    data01 = imp.transform(dataframe)
    processed_data = pd.DataFrame(data01)
    processed_data.to_csv(result)


def random_impute(data,result):#插补随机值
    dataframe=pd.read_csv(data)
    dataframe=np.array(dataframe)
    data01=impyute.imputation.cs.random(dataframe)
    
    
    processed_data = pd.DataFrame(data01)
    processed_data.to_csv(result)
      

def mode_impute(data,result):#模式插补
    dataframe=pd.read_csv(data)
    dataframe=np.array(dataframe)
    data01=impyute.imputation.cs.mode(dataframe)
    processed_data = pd.DataFrame(data01)
    processed_data.to_csv(result)

        
        
def median_impute(data,result):#中位数插补
    dataframe=pd.read_csv(data)
    dataframe=np.array(dataframe)

    data01 =impyute.imputation.cs.median(dataframe) 
    processed_data = pd.DataFrame(data01)
    processed_data.to_csv(result)



def EM_impute(data,result,loop_number):#期望最大化插补
    dataframe=pd.read_csv(data)
    dataframe = np.array(dataframe)
    data01 = impyute.imputation.cs.em(dataframe,loops=loop_number)
    processed_data = pd.DataFrame(data01)
    processed_data.to_csv(result)

def fast_knn_impute(data,result,k,eps,p):#快速KNN插补
    dataframe=pd.read_csv(data)
    dataframe = np.array(dataframe)
    data01 = impyute.imputation.cs.fast_knn(dataframe,k=k,eps=eps,p=p)
    processed_data = pd.DataFrame(data01)    
    processed_data.to_csv(result)

def KNN_impute(data,result):
    dataframe=pd.read_csv(data)
    processed_data = KNN(k=4).fit_transform(dataframe)
    processed_data = pd.DataFrame(processed_data)
    processed_data.to_csv(result)


def IterativeImpute(data,result):
    dataframe=pd.read_csv(data)
    processed_data = IterativeImputer().fit_transform(dataframe)
    processed_data = pd.DataFrame(processed_data)
    processed_data.to_csv(result)

def IterativeSVD_Impute(data,result):
    dataframe=pd.read_csv(data)
    processed_data = IterativeSVD().fit_transform(dataframe)
    processed_data = pd.DataFrame(processed_data)
    processed_data.to_csv(result)

def MatrixFactorization_Impute(data,result):
    dataframe=pd.read_csv(data)
    processed_data = MatrixFactorization().fit_transform(dataframe)
    processed_data = pd.DataFrame(processed_data)
    processed_data.to_csv(result)

def NuclearNormMinimization_Impute(data,result):
    dataframe=pd.read_csv(data)
    processed_data = NuclearNormMinimization().fit_transform(dataframe)
    processed_data = pd.DataFrame(processed_data)
    processed_data.to_csv(result)
