# timeseries
 
Defination:

Time series: A collection of data points collected at constant time intervals.

Propeties:
1. It is time dependent. So the basic assumption of a linear regression model that the observations are independent doesn't hold in this case.
2. Increasing or decreasing trend has some form of seasonality trend, i,e variations specific to a particular time frame.

Is it stationary?
Is there a seasonality?
Is the targer variable autocorrelated?


Autocorrelation:
simalirity between observations as a function of the time lag between them

Seasonality:
Periodic fluctuations.
e,g: electricity consumption is high during the data and low during night, or oline salens
increase during Christmas before slowing down again.

Stationary:
If the statistical properties donot change over time.
constant mean and variance.

and co-variance is independent of time.

How to test if a process is stationary

You may have noticed in the title of the plot above Dickey-Fuller. This is the statistical test that we run to determine if a time series is stationary or not.

Without going into the technicalities of the Dickey-Fuller test, it test the null hypothesis that a unit root is present.

If it is, then p > 0, and the process is not stationary.

Otherwise, p = 0, the null hypothesis is rejected, and the process is considered to be stationary.

Moving Average:
The next observation is the mean of all the past observations.


