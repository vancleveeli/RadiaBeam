# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 09:58:47 2016

@author: Eli Van Cleve
"""
import numpy as np
#import csv
import pandas as pd

#dir = '/mnt/g/Eli/RadiaBeam/SQF/'
dir = 'G:/Eli/RadiaBeam/SQF/'

filename = input ("Enter File Name: ")

save = filename[:-4]+'-clean.csv'
print (dir+filename)

data = pd.read_csv(dir+filename, error_bad_lines=False)

Lsize = len(data.Freq)
#Lsize = len(data.lambda(GHz))
colN = len(data.iloc[0])

colNa = np.array([])
for col in data.columns:
    colNa = np.append(colNa,col)




StoreData = []
dataA = data.to_numpy()

leng = len(dataA)


for i in range(leng):
    if (9 > data.Freq[i] > 4):
        StoreData.append(dataA[i])

df = pd.DataFrame(StoreData, columns = colNa)
print (df)

df.to_csv(dir+save, index = False)
