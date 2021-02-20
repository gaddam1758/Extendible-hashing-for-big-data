from DataGenerator import DataGenerator
import pandas as pd
import numpy as np
from SimulatedSecondaryMemory import SimulatedSecondaryMemory 
from Ex_Hash import ExtendibleHashing



print('-----select-option---')

print('enter record size, directory size')

r_size = int(input())
d_size = int(input())

ssm = SimulatedSecondaryMemory(10000, 20, 20)


print('---SSM Created---')
print('Press 1 ----  a) enter dataset size to insert records')
print('Press 2 ---- b) enter record to insert')


ex_hash = None

while True:
    k = int(input())
    if k == 1:
            data_size = int(input())
            DataGenerator('a.csv',)
            df = pd.read_csv('a.csv')
            X = np.asarray(df)  
            ex_hash = ExtendibleHashing(X,hash,ssm,1024)
            ex_hash.visualize()            
            
    if k == 2:
        t_id = int(input('enter id'))
        amt = int(input('enter sale amount'))
        name = input('enter name')
        cat = int(input('enter category'))
        
        l = [t_id,amt,name,cat]
        
        X = np.assray(l)
        X = np.reshape(X, (1,1))
        


