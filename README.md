# SC-sequencing-imputer
The algrithms and codes use some packages, you should pip them at first.
import numpy as np
import pandas as pd
import fancyimpute
import impyute
import sklearn

This code can achieve the 11 algrithms for the singal-cell sequence data drop
Algrithms are :Mean,MedianMode,Random,Iterative、IterativeSVD、Fastknn、KNN、NuclearNormMinimization、MatrixFactorzation and EM
Before you try to use is,you should make sure that your dataset is .csv format . And you should ensure your file  just containing the number matrix (please delete the data header)


step 1: delete the dataset's header and get the number matrix
step 2: use the divide function to seperate ur file (you can ignore this step)
step 3: use the load_data function .It can achieve the graient_drop_rate with 10 graients(filter) 
step 4: imputer function can carry out 11 algrithms
step 5: evaluate fuction can come up MSE,EVS,R2
