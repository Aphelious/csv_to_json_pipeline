import psycopg2 as db
import pandas as pd


conn_string = "dbname='dataengineering' host='localhost' user='postgres' password='password'"
conn = db.connect(conn_string)
cur=conn.cursor()

query = "SELECT * FROM transactions"

df = pd.read_sql(query, conn)

print(df.head())

