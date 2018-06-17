### Notes on Pandas

* In working with data for machine learning, you can't work with NaN data, often you may find that you need to replace NaN with some dummy data, this will allow you to mark data as missing, without throwing everything away

```python
# An example of replacing NaN data, df is a pandas dataframe
df.fillna(-99999, inplace=True)
```