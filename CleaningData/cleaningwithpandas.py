import pandas as pd

# load in the csv data:
df = pd.read_csv(r'escooter/scooter.csv')

# set display options:
pd.set_option('display.max_columns', 15)

# ## Some simple display methods:
print(df.head())
# print(df.tail())
# print(df.sample(5))
#
# ## Pandas supports some slicing type syntax:
# print(df['DURATION'])
# print(df[['trip_id','DURATION']])
# print(df[:10])
# print(df[10:])
# print(df.columns[3])

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
# ## Can be called on a single column:
# print(df['start_location_name'].describe())

## value_counts() method will return a table of values and their frequency in the dataset:
## Nomalize parameter will return the count as a percentage
# print(df['DURATION'].value_counts(normalize=True))

## isnull() will return bool if a value is null but can be used in conjunction with sum() to get a total:
# print(df.isnull().sum())

## Dropping rows and columns:
# df.drop(columns=['region_id'], inplace=True)    # Drop a whole column
# df.drop(index=[123234], inplace=True)   # Drop a single row

## Drop rows where the start_location_name column is n/a
# df.dropna(subset=['start_location_name'], inplace=True)

## Can drop an entire column if the total number of na is more than a given percentage
# df.dropna(axis='index', thresh=len(df)*.25)

## Can use the fillna method to fill in holes in the data based on different criteria
# print(df.isnull().sum())
# df.fillna(axis='columns', value='00:00:00', inplace=True)
# print(df.isnull().sum())

## Advanced filtering by passing a dict of replacement values into the fillna() method
# start_stop = df[(df['start_location_name'].isnull())&(df['end_location_name'].isnull())]
# value = {'start_location_name':'Start St.', 'end_location_name':'Stop St.'}
# print(start_stop[['start_location_name', 'end_location_name']])
# new_start_stop = start_stop.fillna(value=value)
# print(new_start_stop[['start_location_name', 'end_location_name']])

## Advanced filtering by creating 'sub-dataframes':
# may = df[(df['month']=='May')]
# df.drop(index=may.index, inplace=True)
# print(df['month'].value_counts())

## Formatting dataframe columns and data
# df.columns = [x.lower() for x in df.columns]    # list comprehension to modify the df column names
# print(df.columns)

## Modify
# df['month']=df['month'].str.upper()
# print(df['month'].head())

## Iterate through the dataframe and input a value into each row under a new column
# for i, r in df.head().iterrows():
#     if r['trip_id']==1613335:
#         df.at[i, 'new_column'] = 'Yes'
#     else:
#         df.at[i, 'new_column'] = 'No'
# print(df[['trip_id', 'new_column']].head())

## Splitting columns into new columns using df.str.split()
# started_at = df['started_at'].str.split(expand=True)
# print(started_at.head())
# started_at['date'] = started_at[0]
# started_at['time'] = started_at[1]
# print(started_at['date'])
# print(started_at['time'])

## Handling Datetime object conversion from generic 'object' types
# df['started_at'] = pd.to_datetime(df['started_at'], format='%m/%d/%Y %H:%M')
# print(df.dtypes)
#
# when = '2019-06-23'
# x = df[df['started_at']>when]
# print(len(x))

## Filtering out the top five locations, spliting on street, format adjustment, overwrite original
# new = pd.DataFrame(df['start_location_name'].value_counts().head())
# new.reset_index(inplace=True)
# new.columns=['address', 'count']
# n = new['address'].str.split(pat=',',n=1, expand=True)
# replaced = n[0].str.replace('@', 'and')
# new['street'] = replaced

## Joining two dataframes just like in SQL using the df.join() method:
# geo = pd.read_csv(r'/Users/mike/Desktop/Main/Programming/Projects/Tutorials/dataeng/CleaningData/escooter/geocodedstreet.csv')
# joined = new.join(other=geo, how='left', lsuffix='_new', rsuffix='_geo')
# print(joined[['street_new', 'street_geo', 'x', 'y']])

## Merging is just like a join but duplicate cols are removed, cleaner
# new_geo_merged = pd.merge(new, geo, on='street')
# print(new_geo_merged)


## Pandas can generate table schema based on a dataframe, pass engine from SQLalchemy it will be dialect-specific
# print(pd.io.sql.get_schema(df, name='table_name', con=engine))