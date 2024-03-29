import pandas as pd
import numpy as np
import matplotlib.pylab as plt

from matplotlib.pylab import rcParams

rcParams['figure.figsize']=15,6
data=pd.read_csv('AirPassengers.csv')
print (data.head())
print ('\n Data Types:')
print (data.dtypes)

###conveting the date
dateparse = lambda dates: pd.datetime.strptime(dates,'%Y-%m')
data=pd.read_csv('AirPassengers.csv',parse_dates=['Month'],index_col='Month',date_parser=dateparse)

print (data.head())
print (data.dtypes)
print (data.index)

ts=data['#Passangers']ts.head(10)
print (ts)

print (ts[datetime])