#Now let's analyze ourself!
import pandas as pd_a
from fbprophet import Prophet
import numpy as np


#Basic plotting and graphing to explore the data
data = pd_a.read_excel("MFPClean.xlsx")
data["weigh_in_date"] = pd_a.to_datetime(data["weigh_in_date"])
data = data.sort_values(by="weigh_in_date")
data.set_index('weigh_in_date')['weight'].plot();
data['weight'].plot(kind='hist', bins=20)
data.set_index('weigh_in_date')['weight'].plot(kind='kde');
df = pd_a.DataFrame({'x': data["weight"], 'y': data["weight"]})
ax = df.plot.hexbin(x='x', y='y', gridsize=12)
data.describe(percentiles=[0,1/10, 2/10, 3/10,4/10,5/10,6/10,7/10,8/10,9/10])

# Prophet requires columns ds (Date) and y (value)
m = data.rename(columns={'weigh_in_date': 'ds', 'weight': 'y'})
n = Prophet()
n.fit(m)
future = n.make_future_dataframe(periods=1825)
future.tail()
forecast = n.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
fig1 = n.plot(forecast)
fig2 = n.plot_components(forecast)

