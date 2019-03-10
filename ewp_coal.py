# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 08:51:55 2019

@author: beomc
"""

### ewp coal data, dtypes , joins  


## python

"""
import csv  # module
 
f = open('data.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
   print(line)
f.close()    
"""

## pandas
import pandas as pd
import numpy as np
 
## index column 

# df = pd.read_csv('C:/Users/beomc/working/ewp/ewp_rawdata/data_coal_state_2.csv', index_col='c1') 

df = pd.read_csv('C:/Users/beomc/working/ewp/ewp_rawdata/data_coal_state_2.csv') 

df.head()
df.dtypes

## slice test

df1 = pd.DataFrame(df) # make Series or DataFrame 
df1.dtypes # c1 = object 

df1[ : 2] # [2 rows x 124 columns]

df1.loc [0:, "c1": "c2"] # label of column

df1.loc[ : 0]
df1.iloc[1] # extract row 
df1.loc[0] # extract row 


df1_c1 = df1(["c1", "c2"]) # extract column c1  


df1["c1"] = df1["c1"].astype('datetime64[ns]') # make datetimeIndex 

df1 = df1.asfreq(freq='10min', method='pad')




## pre exercise
 
df1.dtypes # c1 = object 
 
np.dtype('datetime64[ns]') == np.dtype('<M8[ns]')

# convert a column's dtypes

s = pd.Series(["8", 6, "7.5", 3, "0.9"]) # mixed string and numeric values
pd.to_numeric(s) # convert everything to float values

# convert column "a" of a DataFrame
df1["a"] = pd.to_numeric(df1["c1"])

df1 = df1.astype({"c1": int, "c2": complex})

pd.to_datetime(pd.Series(['05/23/2005'])) ## **
df['date'] = df['date'].astype('datetime64[ns]')


# 1. DatetimeIndex (pd . to_datetime ) --> Series or DataFrame  

s = pd.to_datetime(df)

# 2. Series data
s1 = pd.Series(df['c1'])
 

s1 = s.asfreq(freq='10min', method='pad')

 
## DataFrame slice


dates = pd.date_range('1/1/2019', periods=5)

##

dates.dtype

s = pd.Series([1, 2], dtype='int32')
s
 
s.astype('int64')


df1 = pd.DataFrame(np.random.randn(5, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df1 = pd.DataFrame(np.random.randint(5, size=(5, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
df1

s = df1['A']
s

df1[['A', 'B']]

df2 = df1.asfreq(freq='10m')
df2

## join


