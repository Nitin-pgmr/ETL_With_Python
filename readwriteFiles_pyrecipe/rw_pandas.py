import pandas as pd

df=pd.read_csv('data.CSV')
print(df)

# write to a csv file from dict using Pandas
data={'Name':['Paul','Bob','Susan','Yolanda'],
'Age':[23,45,18,21]}
df_dict=pd.DataFrame(data)
df_dict.to_csv('fromdf.CSV',index=False)