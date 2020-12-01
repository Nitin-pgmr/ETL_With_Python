import psycopg2 as db
conn_string="dbname='dataengineering' host='localhost' user='postgres' password='test123'"
conn=db.connect(conn_string)
cur=conn.cursor()
query = "select * from users"
cur.execute(query)
#for record in cur:
    #print(record)
cur.fetchall()
cur.fetchmany(10)
data=cur.fetchmany(1)

print("total count{0} ".format(cur.rowcount));
print("rownumber{0} ".format(cur.rownumber));
conn=db.connect(conn_string)
cur=conn.cursor()
f=open('fromdb.csv','w')
cur.copy_to(f,'users',sep=',')
f.close()
f=open('fromdb.csv','r')
print(f.read())
