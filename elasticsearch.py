from elasticsearch import Elasticsearch
import requests
import json

r = requests.get('http://localhost:9200')
i = 1

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


while r.status_code == 200:
    r = requests.get('http://swapi.co/api/people/' + str(i))
    es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    i = i + 1

print(i)
