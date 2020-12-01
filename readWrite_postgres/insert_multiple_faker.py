import psycopg2 as db
from faker import Faker

fake=Faker()
data=[]
i=2

for r in range(1000):
    data.append((i,fake.name(),fake.street_address(),
    fake.city(),fake.zipcode()))
    i+=1

data_for_db = tuple(data)
conn_string="dbname='dataengineering' host='localhost' user='postgres' password='test123'"
conn=db.connect(conn_string)
cur=conn.cursor()
query = "insert into users (id,name,street,city,zip) values(%s,%s,%s,%s,%s)"

print(cur.mogrify(query,data_for_db[1]))
cur.executemany(query,data_for_db)
conn.commit()