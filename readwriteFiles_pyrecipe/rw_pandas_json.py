import pandas.io.json as pd_JSON

f=open('data.JSON','r')
data=pd_JSON.loads(f.read())

df=pd_JSON.json_normalize(data,record_path='records')
print(df)

print(df.head(2).to_json())
