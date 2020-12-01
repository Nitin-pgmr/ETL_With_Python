import pandas as pd

def CSVToJson():
    df=pd.read_csv('C:/Users/nitin/Desktop/linda/DataEngineering/etl_python/venv/readwriteFiles_pyrecipe/data.CSV')
    for i,r in df.iterrows():
        print(r['name'])
    df.to_json('fromAirflow.JSON',orient='records')


CSVToJson()