### pandas - DataFrame

## https://www.tutorialspoint.com/python_pandas/python_pandas_groupby.htm 
import pandas as pd
import numpy as np

### class DataFrame

##  DataFrame  
### slice , join 

data = { "key1" : [ 0, 1, 2, 3], "name" : ["lee", "park", "seo", "lee"]}

df =pd.DataFrame(data, columns= ["name", "key1"], index=[0,1,2, 3])
df 
df["name"] # 1
df.name   # 2
df["new_c1"] = 5 # 3
df["new_c2"] = [1,2,3,5] # 4
df[["key1", "new_c2"]]  # 5
df["new_c1"] = np.arange(4) # 6 : 0~ n-1

df.columns
df.index.name ="no"
df.columns.name ="variables"

### slice 

df.loc[0:1, "name"]  # "name" 
df.loc[0:1, ["name", "key1"]] # "name", "key1"
df.loc[2]


### join

caller = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                       'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})

other = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                      'B': ['B0', 'B1', 'B2']})

caller
other

# Join DataFrames using their indexes.
caller.join(other, lsuffix='_caller', rsuffix='_other')


### append

df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
df2
df3 = pd.DataFrame([[15, 16], [17, 18]], columns=list('cd'))
df3

df.append(df2)
df.append(df2, ignore_index=True)
df.append(df3)



### 
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=d)
df

df2 = pd.DataFrame(np.random.randint(low=0, high=10, size=(5, 5)),
                   columns=['a', 'b', 'c', 'd', 'e'])
df2
df2.dtypes
df2.head()
##
dates = pd.date_range('20190101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

df.index
df.columns
df.values
df.describe()
# Transposing your data
df.T
df.sort_index(axis=1, ascending=False)

df['A']
df[0:3]
df['20190101':'20190104']
# For getting a cross section using a label:
df.loc[dates[0]]
df.loc[:,['A','B']]

# 
rng = pd.date_range('1/1/2019', periods=10, freq='H')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts.head() 
rng
## 
df5 = pd.DataFrame({"A":[1,2,3], "B":[4,5,6], "C":[7,8,9]})
df5
df5.iloc[0]
df5.loc[0]

df[0]
 
df = pd.DataFrame({'a': pd.date_range('2019-01-01', '2019-12-31'), 'b': range(365)})
df

df.groupby(df.a.dt.month).b.count()

## series

s = pd.Series([3, 5, 7, 9], index=['a', 'b', 'c', 'd'])
print(s)

s = pd.Series([1,3,5,np.nan,6,8])
dates = pd.date_range('20130101', periods=6)





##

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print(df)

print(df.groupby('Team').groups)
 
#

grouped = df.groupby('Year')

for name,group in grouped:
    print(name)
    print(group)

grouped.dtypes

print(grouped.get_group(2014))

# groupby('Team')   -> 

grouped = df.groupby('Team')

print(grouped.get_group('Riders'))


# aggregation

import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby('Year')

print(grouped['Points'].agg(np.mean))
print(grouped.agg(np.size))

grouped = df.groupby('Team')
print(grouped.agg(np.size))
print(df)

# 
print(grouped['Points'].agg([np.sum, np.mean, np.std]))

# transformation , lamda

grouped = df.groupby('Team')
score = lambda x: (x - x.mean()) / x.std()*10
print(grouped.transform(score))

# filter 
print(df.groupby('Team').filter(lambda x: len(x) >= 3))
