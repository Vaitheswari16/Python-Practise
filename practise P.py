"""import pandas as pd
df=pd.read_csv('data.csv')

pd.options.display.max_rows
print(df.to_string)
"""


#  simple pandas series from a list

"""
import pandas as pd

a=[1,2,3,3]
myvar=pd.Series(a)
print(myvar)

myvar=pd.Series(a,index=['x','y','z','a']) #-------lables
print(myvar)
"""
#---JSON
"""
import pandas as pd
df=pd.read_json("data.json")
print(df.head(1))
print(df.tail(2))
print(df.info())
"""
#-----key value series
""""
import pandas as pd
calories={"day1":220,"day2":340,"day3":560}
myvar=pd.Series(calories)
print(myvar)

myvar=pd.Series(calories,index=["day1","day2"])
print(myvar)
"""
#---Dataframe----
""""
import pandas as pd 
data={
    "callories":[20,30,40],
    "duration":[10,20,30]
}

df=pd.DataFrame(data)
print(df)
print(df.loc[[0,1]])
df=pd.DataFrame(data,index=['day1','day2','day3'])
print(df)
print(df.loc[['day1','day2']])
"""

""""
import pandas as pd
df = pd.read_csv('data2.csv')
df.dropna(inplace=True)
print(df.to_string())

import pandas as pd
df=pd.read_csv('data2.csv')
df.fillna(130,inplace=True)
print(df.to_string())

import pandas as pd

df = pd.read_csv("data2.csv")

print(df.isna().sum())
print(df.dtypes)

"""
""""
import pandas as pd
df=pd.read_csv("data2.csv")
df.fillna({"Salary":3000},inplace=True)
print(df.to_string())
"""
#-----MEAN--------
"""
import pandas as pd

df=pd.read_csv("data2.csv")
x=df["Salary"].mean()
df.fillna({"Salary":x},inplace=True)
print(df.to_string())

"""
#MEDIAN-------------
""""
import pandas as pd

df=pd.read_csv("data2.csv")
x=df["Salary"].median()
df.fillna({"Salary":x},inplace=True)
print(df.to_string())

#-----MODE
import pandas as pd

df=pd.read_csv("data2.csv")
x=df["Salary"].mode()[0]
df.fillna({"Salary":x},inplace=True)
print(df.to_string())

"""
#DATE---------
"""
import pandas as pd

df=pd.read_csv("data2.csv")
df['JoinDate']=pd.to_datetime(df['JoinDate'],  errors="coerce")
print(df.to_string())

invalid_rows = df[df["JoinDate"].isna()]
print(invalid_rows)

#df["JoinDate"] = df["JoinDate"].fillna("2023-01-01")

df.dropna(subset=['JoinDate'],inplace=True)
print(df.to_string())
"""

#location
""""
import pandas as pd

df=pd.read_csv("data2.csv")
df.loc[10,'JoinDate']=2023-7-7
print(df.to_string())

"""""
"""
import pandas as pd

df=pd.read_csv("data2.csv")

for x in df.index:
    if df.loc[x,'Salary']>1000:
        df.loc[x,'Salary']=2000
print(df.to_string())

for x in df.index:
    df.loc[x,'Salary']<2000
    df.drop(x,inplace=True)
print(df.to_string())
"""

#---Matplotlib------


"""""
#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data.csv")
df.plot()
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('data.csv')
df.plot(kind='scatter',x='id',y='salary')
plt.show()