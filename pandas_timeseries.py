### time series 

import pandas as pd
import numpy as np

date_str = ["2018, 1, 1", "2018, 1, 4"]
idx = pd.to_datetime(date_str)
idx

# make series or DataFrame

np.random.seed(0)

s = pd.Series(np.random.randn(4), index=idx)
s = pd.Series(np.random.randint(5, size=(2)), index=idx)
s

s1 = s.asfreq(freq='10min', method='pad')
s1

##

s2 = pd.date_range("2019-1-1", "2019-1-2", freq="10T")
s2

