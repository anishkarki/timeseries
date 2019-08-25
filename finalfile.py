import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.metrics import r2_score,median_absolute_error,mean_absolute_error,mean_squared_error,mean_squared_log_error

from scipy.optimize import minimize
import statsmodels.tsa.api as smt
import statsmodels.api as sm

from tqdm import tqdm_notebook
from itertools import product

def mean_absolute_percentage_error(y_true,y_pred):
    return np.mean(np.abs((y_true-y.pred)/y_true))*100
    
import warnings
warnings.filterwarnings('ignore')

DATAPATH='AirPassengers.csv'

data=pd.read_csv(DATAPATH,index_col=['Month'],parse_dates=['Month'])
print (data.head(10))

plt.figure(figsize=(17,8))
plt.plot(data.Passengers)
plt.title('the size of the database per months')
plt.ylabel('Storage size')
plt.xlabel('months')
plt.grid(False)
#plt.show()

#This is not stationary process and it is hard to tell if there is some kind of seasonality
#moving average

def plot_moving_average(series,window,plot_intervals=False,scale=1.96):
    rolling_mean=series.rolling(window=window).mean()
    plt.figure(figsize=(17,8))
    plt.title('moving average\n window size = {}'.format(window))
    plt.plot(rolling_mean,'g',label='Rolling mean trend')
    plt.show()
    
    #plot confidence interals for smoothed values
    if plot_intervals:
        mae=mean_absolute_error(series[window:],rolling_mean[window:])
        deviation=np.std(series[window:] - rolling_mean[window:])
        lower_bound = rolling_mean - (mae + scale*deviation)
        upper_bound = rolling_mean + (mae + scale*deviation)
        plt.plot(upper_bound, 'r--', label = 'Upper bound/Lower bound')
        plt.plot(lower_bound,'r--')

    plt.plot(series[window:], label='Actual values')
    plt.legend(loc='best')
    plt.grid=(True)
    plt.show()
    

plot_moving_average(data.Passengers,3)
plot_moving_average(data.Passengers,3,plot_intervals=True)