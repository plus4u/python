# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 20:47:53 2019

@author: beomc
"""
## time series 

import pandas as pd
from datetime import datetime
import numpy as np
date_rng = pd.date_range(start='1/1/2018', end='1/08/2018', freq='H')

date_rng

print(date_rng)

type(date_rng[0])

df = pd.DataFrame(date_rng, columns=['date'])
df['data'] = np.random.randint(0,100,size=(len(date_rng)))
df.head(15)

len(date_rng)

#

df['datetime'] = pd.to_datetime(df['date'])
df = df.set_index('datetime')
df.drop(['date'], axis=1, inplace=True)
df.head()


# 

string_date_rng_2 = ['June-01-2018', 'June-02-2018', 'June-03-2018']
timestamp_date_rng_2 = [datetime.strptime(x,'%B-%d-%Y') for x in string_date_rng_2]
timestamp_date_rng_2


## https://pandas.pydata.org/pandas-docs/stable/timeseries.html  

# 72 hours starting with midnight Jan 1st, 2011
rng = pd.date_range('1/1/2011', periods=72, freq='H')

ts = pd.Series(np.random.randn(len(rng)), index=rng)

ts.head()

# to 45 minute frequency and forward fill
converted = ts.asfreq('45Min', method='pad')

converted.head()

#
pd.Timestamp(datetime(2012, 5, 1))


pd.Timestamp('2012-05-01')


pd.Timestamp(2012, 5, 1)


# Providing a Format Argument

pd.to_datetime('2018/11/12', format='%Y/%m/%d')

pd.to_datetime('12-11-2010 00:00', format='%d-%m-%Y %H:%M')


## time delta

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
print(df)


## operations

s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
df['C']=df['A']+df['B']

print(df)

## read csv
## https://datascienceschool.net/view-notebook/c5ccddd6716042ee8be3e5436081778b/ 

%%writefile sample1.csv
c1, c2, c3
1, 1.11, one
2, 2.22, two
3, 3.33, three
# Writing sample1.csv

#

pd.read_csv('sample1.csv')

# 
df.to_csv('sample6.csv')








## not yet check 
import pandas as pd

### time series

from datetime import datetime

datetime(year=2015, month=7, day=4)

# parse dates from a variety of string formats:

from dateutil import parser
date = parser.parse("4th of July, 2015")
date

#
date.strftime('%A')

date = parser.parse("9th of January, 2019")
date

#
date.strftime('%A')

#

d = pd.to_datetime([datetime(2015, 7, 3), '4th of July, 2015',
                       '2015-Jul-6', '07-07-2015', '20150708'])
d


### compare line plot same interval
import pandas as pd
from pandas import Series
from matplotlib import pyplot



series = Series.from_csv('daily-minimum-temperatures-in-me.csv', header=0)
print(series.head())

series.plot(style='k.')
pyplot.show()

# dataset에 ? 삭제하니  data type 문제해결됨 

series.columns # no attribute 'columns'
series.columns=["date", "temp"]

series=series.astype(float) 
# convert a series to numeric
pd.to_numeric(series, errors='coerce')

# eop


## 
import matplotlib as plt
from pandas import Series
from pandas import DataFrame
from pandas import TimeGrouper
from matplotlib import pyplot

# series = Series.from_csv('daily-minimum-temperatures.csv', header=0)

plt.rcParams["figure.figsize"] = (16,4)


groups = series.groupby(TimeGrouper('A'))
years = DataFrame()
for name, group in groups:
	years[name.year] = group.values
years.plot(subplots=True, legend=False)
pyplot.show()
 

### python

from datetime import date
d = date.fromordinal(730920) # 730920th day after 1. 1. 0001

d # datetime.date(2002, 3, 11)

t = d.timetuple()

for i in t:
    print(i)


from datetime import datetime, date, time
# Using datetime.combine()
d = date(2005, 7, 14)
t = time(12, 30)
datetime.combine(d, t)


datetime.now()   

dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")




