import pandas as pd
import quandl
import math, datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



#Get stock data from Quandl API and create DataFrame
df = quandl.get('WIKI/GOOGL')

#We only need the Adjusted Close
df = df[['Adj. Close']]

#Create our forecast column variable
forecast_col = 'Adj. Close'

#Fill in missing data with outlier
df.fillna(-99999, inplace=True)

#Create our label and window data (x are features, y is target)
forecast_out = int(math.ceil(0.1*len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'],1))
X = X[:-forecast_out]
X_lately = X[-forecast_out:]
X = preprocessing.scale(X)

df.dropna(inplace=True)
y = np.array(df['label'])


#Setup cross-validation for 80/20 split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.2)

#Define and fit the Linear Regression model
#Since the feature and the label are the same, it's really time series
#'n_jobs' makes it multi-threaded, '-1' is the max for the processor
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)

#Check accuracy
accuracy = clf.score(X_test,y_test)

forecast_set = clf.predict(X_lately)


print(df.tail)
print(forecast_set, accuracy, forecast_out)

#Create forecast column
df['Forecast'] = np.nan

#Setup our dates
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]



#Create our charts
style.use('ggplot')
df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

