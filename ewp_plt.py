#-*- coding: utf-8 -*-

import sys
# from importlib import reload
sys.setdefaultencoding('utf-8')

"""
Created on Wed Jan  9 06:25:26 2019

@author: beomc
"""

### 1.exercise  2. data_01_2days_v3.xlsx

# from __future__ import unicode_literals
# from collections import Counter

import matplotlib.pyplot as plt


def make_simple_line_chart():
    """ 그림 3-1. 간단한 선 그래프 """

    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    # create a line chart, years on x-axis, gdp on y-axis
    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

    # add a title
    plt.title("명목 GDP")

    # add a label to the y-axis
    plt.ylabel("Billions of $")
    plt.show()
    
make_simple_line_chart()


## time series 

import numpy as np 
# import pylab as plt 


# Create some sample "time-series" data 
N = 200 
T = np.linspace(0, 5, N) 
Y1 = T**2 - T*np.cos(T*5) + np.random.random(N) 
Y2 = T**2 - T*np.sin(T*5) + np.random.random(N) 

pargs = {"lw":5, "alpha":.6} 

plt.plot(T,Y1, 'r',**pargs) 
plt.plot(T,Y2, 'b', **pargs) 

skip = 30 
plt.scatter(T[::skip],Y2[::skip], color='k', s=200, alpha=.6) 

plt.xlabel("time") 
plt.ylabel("money") 
plt.axis('tight') 

# Save as a png and a pdf 
plt.savefig("example.png") 
plt.savefig("example.pdf") 

plt.show() 


## excel 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('data_01_2days_v3.xlsx')

data.head(5)

# plot : no response 

plt.figure(figsize=(8, 4))
plt.plot(data.ts, data.a)
# plt.plot(data.ts, data.b)
# plt.plot(data.ts, data.c)

plt.grid()
plt.show()

# eop

# Get the figure and the axes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('data_01_2days_v3.xlsx')

data.head(5)
data2 = data[['a', 'b', 'c']]

data2.plot()
plt.show()

## box plot
data2.boxplot()

plt.figure(figsize=(12, 4))

# 첫번째 그래프
# plt.plot(data.t, data.a) # 선 그래프
# plt.ylim([300,400]) # y축의 값을 지정




## 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 그래프를 그릴 X, Y 값을 입력합니다.
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,3,4,6,7,9,10,16,17,20]

# Get the figure and the axes
fig, (ax0, ax1) = plt.subplots(nrows=1,ncols=2, sharey=False, figsize=(8, 4))

# 첫번째 그래프
ax0.plot(x,y) # 선 그래프
ax0.set_ylim([2,20]) # y축의 값을 지정
ax0.set(title='First', xlabel='Score', ylabel='Time')

# 두번째 그래프
ax1.bar(x,y) # 막대 그래프
ax1.set_ylim([0,30])
ax1.set(title='Second', xlabel='Score', ylabel='Time')

# Title the figure
fig.suptitle('TEST', fontsize=14, fontweight='bold')



## 
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import random

fig = plt.figure()
fig.subplots_adjust(bottom=0.2)
ax = fig.add_subplot(111)

N=3*10**6
delta=np.random.normal(size=N)
vf=np.random.normal(size=N)
dS=np.random.normal(size=N)

idx=random.sample(range(N),1000)

plt.scatter(delta[idx],vf[idx],c=dS[idx],alpha=0.7,cmap=cm.Paired)
plt.show()
# eop

data.describe()

### read csv



data3 = pd.read_csv('data_time.csv')
data3.head()

data3['datetime'] = pd.to_datetime(data3.datetime)
data3 = data3.set_index('datetime')


data3.resample('d').mean().plot()

data3['day'] = data3.index.day
data3['hour'] = data3.index.hour
data_by_day = data3.resample('h').mean().set_index(['day', 'hour']).unstack('day')
data_by_day['hash_rate'].plot()
data_by_day['shares'].plot()

data_by_day.head()


### 3. 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# error  to eod

# days, impressions = np.loadtxt("page-impressions.csv", unpack=True,
#        converters={ 0: mdates.strpdate2num('%Y-%m-%d')})


# add convert
def convert_date(date_bytes):
    return mdates.strpdate2num('%y/%m/%d')(date_bytes.decode('ascii'))


date, open, close = np.loadtxt('000001.csv',delimiter=',',
                               converters={0: convert_date},
                               skiprows=1, usecols=(0,1,4), unpack=True)

days, impressions = np.loadtxt("page-impressions.csv", unpack=True,
        converters={0: convert_date}, skiprows=1)


days[0:2]

plt.plot_date(x=days, y=impressions)

plt.show()

## eod


## set_index

np.random.seed(0)
df1 = pd.DataFrame(np.vstack([list('ABCDE'),
                              np.round(np.random.rand(3, 5), 2)]).T,
                   columns=["C1", "C2", "C3", "C4"])

df1

### time interval : data_time.csv

import pandas as pd

data = pd.read_csv('data_time.csv')
data['datetime'] = pd.to_datetime(data.datetime)
data = data.set_index('datetime')


data.resample('d').mean().plot()

data['day'] = data.index.day
data['hour'] = data.index.hour

data.head()

data_by_day = data.resample('h').mean().set_index(['day', 'hour']).unstack('day')

data_by_day.head()
data_by_day.info()

data_by_day['hash_rate'].plot()
data_by_day['shares'].plot() 


### 2. 

data = pd.read_excel('data_01_2days_v3.xlsx')

data.info()

data = data.set_index(pd.DatetimeIndex(data['ts']))

data.head()

data['day']=data.index.day
data['hour']=data.index.hour

data.info()

data.plot(x='hour', y='a', kind='line')
data.plot(x='hour', y='b', kind='scatter')
data.plot(x='hour', y='c', kind='scatter', legend='True')

plt.plot_date(x=days, y=impressions)

### 3 groupby : 미 테스트
import pandas as pd
from pandas import Series  # class
from pandas import DataFrame
from matplotlib import pyplot
from pandas import Grouper   # class

series = Series.from_csv('daily-minimum-temperatures-in-me.csv', header=0)

series.head()
series.dtypes



groups=series.Grouper(key='A')
groups.head()

years = DataFrame()

for name, group in groups:
	years[name.year] = group.values
years.boxplot()
pyplot.show()



### 4. Pandas Series to Excel

import numpy as np
import pandas as pd

s = pd.Series([1,3,5,np.nan,6,8])
 
writer = pd.ExcelWriter('test.xlsx')

s.to_excel(writer,'Sheet1')
s.to_excel(writer,'Sheet2')

writer.save()

# end 



