### file,  DataFrame, class,  join ,  Series, asreq   

import pandas as pd


### file 

from pandas import ExcelWriter

from pandas import ExcelFile

df = pd.DataFrame({'a':[1,3,5,7,4,5,6,4,7,8,9],
                   'b':[3,5,6,2,4,6,7,8,7,8,9]})

writer = ExcelWriter('Pandas_Ex1.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()


### DataFrame

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})

### class

class display(object):
    """Display HTML representation of multiple objects"""
    template = """<div style="float: left; padding: 10px;">
    <p style='font-family:"Courier New", Courier, monospace'>{0}</p>{1}
    </div>"""
    def __init__(self, *args):
        self.args = args
        
    def _repr_html_(self):
        return '\n'.join(self.template.format(a, eval(a)._repr_html_())
                         for a in self.args)
    
    def __repr__(self):
        return '\n\n'.join(a + '\n' + repr(eval(a))
                           for a in self.args)

#
display('df1', 'df2')


### one-to-one joins

df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})

df3 = pd.merge(df1, df2)

### Many-to-one joins
df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                    'supervisor': ['Carly', 'Guido', 'Steve']})
    
### display
    
from IPython.display import display, HTML 

display(df1) 

# from IPython.display import HTML # <IPython.core.display.HTML object>
display(HTML(df2.to_html())) 


### Series
  
import numpy as np

data = np.array(['a','b','c','d'])
s = pd.Series(data)


pd.Series(range(10, 14))

s = pd.Series([9904312, 3448737, 2890451, 2466052],
              index=["서울", "부산", "인천", "대구"])

print(s)

s["부산":"대구"]

s2 = pd.Series({"서울": 11, "부산": 22, "인천": 33, "대전": 44})

print(s2)

### asreq

index = pd.date_range('1/1/2019', periods=4, freq='T')
s = pd.Series([0.0, None, 2.0, 3.0], index=index)
df = pd.DataFrame({'s':s})
df

df.asfreq(freq='30S')
df.asfreq(freq='30S', fill_value=9.0)
df.asfreq(freq='30S', method='bfill')


#

index_values = (pd.date_range('1/1/2019', 
                   periods=3,freq='W')) 
  
# Creating a series using 'index_values' 
# Notice, one of the series value is nan value 
series = (pd.Series([0.0,None,2.0], 
              index=index_values)) 
  
# Creating dataframe using the series 
df=pd.DataFrame({"Col_1":series}) 
  
# Print the Dataframe 
df 

# unsampling and providing a fill value of 100.0 
df.asfreq(freq ='D', fill_value = 100.0) 

##


