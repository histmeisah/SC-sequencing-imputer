import pandas as pd
import numpy as np
import sklearn
from sklearn.metrics import explained_variance_score, max_error, mean_squared_error, mean_squared_log_error, r2_score
from sklearn import preprocessing



def ravel_data(data):
    
    data=pd.read_csv(data,delimiter=",")
    data=np.array(data)
    data=np.ravel(data)
    (m,)=data.shape
    data=data.reshape(m,1)
    return data
def evaluate(n):#n为选取的算法数目
    algset={1:'raw_data',2:'mean',3:'median',4:'mode',5:'random',6:'I',7:'ISVD',8:'fastknn',9:'KNN',10:'NNM',11:'MF',12:'EM'}
    for i in range(1,n+2):
        algset[i]=ravel_data(data=algset[i]+'.csv')
    
    A=np.zeros((n+1,n+1))
    B=np.zeros((n+1,n+1))
    C=np.zeros((n+1,n+1))
    
    for i in range(1,n+2):
        for j in range(1,n+2):
            A[i-1][j-1]=r2_score(algset[i],algset[j])
            B[i-1][j-1]=mean_squared_error(algset[i],algset[j])
            C[i-1][j-1]=explained_variance_score(algset[i],algset[j])
    with open('r2_score.csv','wb'):
        np.savetxt('r2_score.csv',A,delimiter=',')
    with open('MSE.csv','wb'):
        np.savetxt('MSE.csv',B,delimiter=',')
    with open('EVS.csv','wb'):
        np.savetxt('EVS.csv',C,delimiter=',')
