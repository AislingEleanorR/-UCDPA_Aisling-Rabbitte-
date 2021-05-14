import pandas as pd

data = pd.read_csv("country_wise_latest.csv")
sorted = data.sort_values('WHO Region', ascending=True)
print(sorted.columns)

print(sorted.dtypes)

print(sorted.head())

print(sorted.tail())
