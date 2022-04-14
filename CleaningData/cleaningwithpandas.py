import pandas as pd

# load in the csv data:
df = pd.read_csv(r'escooter/scooter.csv')

# set display options:
# pd.set_option('display.max_columns', 15)

## Some simple display methods:
print(df.head())
print(df.tail())
print(df.sample(5))

## Pandas supports some slicing type syntax:
print(df['DURATION'])
print(df[['trip_id','DURATION']])
print(df[:10])
print(df[10:])
