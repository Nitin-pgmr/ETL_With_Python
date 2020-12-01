import psycopg2 as db
import pandas as pd
conn_string="dbname='dataengineering' host='localhost' user='postgres' password='test123'"
conn=db.connect(conn_string)

df=pd.read_sql("select * from users", conn)
df.to_json(orient='records')
print(df)