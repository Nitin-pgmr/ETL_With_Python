from elasticsearch import Elasticsearch
es = Elasticsearch()
doc={"query":{"match_all":{}}}

res=es.search(index="users",body=doc,size=10)
print(res['hits']['hits'])
for doc in res['hits']['hits']:
    print(doc['_source'])