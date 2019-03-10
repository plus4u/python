# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:46:19 2019

@author: beomc
"""

### 1. matplotlib  2. pandas  3. numpy

# sphinx_gallery_thumbnail_number = 3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure()  # an empty figure with no axes
fig.suptitle('No axes on this figure')  # Add a title so we know which it is

fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

##
a = pd.DataFrame(np.random.rand(4,5), columns = list('abcde'))
a_asndarray = a.values

a.head()

a_asndarray


## 2. pandas

s = pd.Series(range(10, 14))
s
s.index

s.name='tem'
s.index.name='id'

## dataframe class 
data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2431774] }

data.dtypes

## stddev
import pandas as pd

dat = pd.DataFrame({'x1': [1,2,3,4,0,0,0],
                    'x2': [10,12,13,14,15,16,17]})
dat

dat=pd.DataFrame()

print(dat['x1'].values.var())
print(dat['x2'].var())


dat['mean']=dat.mean()
dat['stddev']=dat.std()

print(dat['x'].values.var())
print(dat['x'].var())

#
import numpy as np
 
print(np.var([5,5,5,6,5,5]))
print(np.std([5,5,5,6,5,5]))

#

import pandas as pd
import numpy as np
 
#Create a DataFrame
d = {
    'Name':['Alisa','Bobby','Cathrine','Madonna','Rocky','Sebastian','Jaqluine',
   'Rahul','David','Andrew','Ajay','Teresa'],
   'Score1':[62,47,55,74,31,77,85,63,42,32,71,57],
   'Score2':[89,87,67,55,47,72,76,79,44,92,99,69],
   'Score3':[56,86,77,45,73,62,74,89,71,67,97,68]}
 
 
 
df = pd.DataFrame(d)

print(df)

d1=df.var()

d1


## resample  groupby
import pandas as pd

index = pd.date_range('1/1/2000', periods=9, freq='T')
series = pd.Series(range(9), index=index)
series

series.resample('3T', how='sum')

series.resample('3T', how='sum', label='right')


series.resample('3T',label='right', closed='right').sum()

## groupby
import pandas as pd
import numpy as np
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})

grouped = df.groupby('A')

grouped = df.groupby(['A', 'B'])
grouped.sum()

## 3. numpy

b = np.matrix([[1,2],[3,4]])
b_asarray = np.asarray(b)


# 

x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)

x

type(x)

x.shape

x.dtype

x[1, 2] # The element of x in the *second* row, *third* column, namely, 6.


x[0, 0]


