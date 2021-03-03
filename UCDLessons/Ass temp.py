import pandas as pd
import numpy as np
import datetime

df = pd.DataFrame({'column name':[1500000000000.0,1500000000000.0]})
print (df['column name'])
#df['column name'] = df['column name'].astype(np.int64)
#df['column name'] = df['column name'].astype(int)
#print (df['column name'])

df['column name'] = pd.to_datetime(df['column name']/1000, unit='s')
#df['column name2'] = datetime.datetime.fromtimestamp(df['column name']/1000)
print (df['column name'])