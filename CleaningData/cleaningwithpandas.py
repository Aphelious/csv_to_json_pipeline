import pandas as pd

# load in the csv data:
df = pd.read_csv(r'escooter/scooter.csv')

# set display options:
pd.set_option('display.max_columns', 15)

# ## Some simple display methods:
# print(df.head())
# print(df.tail())
# print(df.sample(5))
#
# ## Pandas supports some slicing type syntax:
# print(df['DURATION'])
# print(df[['trip_id','DURATION']])
# print(df[:10])
# print(df[10:])
#
# ## Pandas Where, Loc, At methods:
# print(df.loc[182])  ## Prints the whole row at index 182
# print(df.at[182, 'DURATION'])   ## Prints the value of DURATION column at index 182
# print(df.where(df['user_id']==186443))  ## Returns rows that match the condition
#
# ## Can create compound statements with where and ampersand
# one = df['user_id']==186443
# two = df['trip_ledger_id']==123234
# print(df.where(one & two))
# # Also:
# print(df[(one) & (two)])

## Describe method outputs basic distribution statistics but is not always apporpriate.
# print(df.describe())
#
# ## Can be called on a single column:
# print(df['start_location_name'].describe())

## value_counts() method will return a table of values and their frequency in the dataset:
# print(df['DURATION'].value_counts(normalize=True))

## isnull() will return bool if a value is null but can be used in conjunction with sum() to get a total:
# print(df.isnull().sum())

## Dropping rows and columns:
# df.drop(columns=['region_id'], inplace=True)    # Drop a whole column
# df.drop(index=[123234], inplace=True)   # Drop a single row

## Drop rows where the start_location_name column is n/a
# df.dropna(subset=['start_location_name'], inplace=True)

## Can drop an entire column if the total number of na is more than a given percentage
df.dropna(axis='index', thresh=len(df)*.25)


