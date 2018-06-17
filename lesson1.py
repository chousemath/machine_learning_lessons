import pandas as pd
import quandl
import math

df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High',
         'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = 100 * (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close']
df['PCT_CHANGE'] = 100 * (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']
# extract only the desired columns
df_wanted = df[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]
forecast_column = 'Adj. Close'
# in machine learning, you can't work with NaN data, need to replace NaN
# this will allow you to mark data as missing, without throwing everything away
df_wanted.fillna(-99999, inplace=True)
# this next variable determines how far out into the past you want to include data
forecast_out = int(math.ceil(0.01 * len(df_wanted)))
# shift the rows of the forecast column 'up'
df_wanted['label'] = df_wanted[forecast_column].shift(forecast_out)
print(df_wanted.tail())
