# Import Elasticsearch package
from elasticsearch import Elasticsearch
# Connect to the elastic cluster
es = Elasticsearch([{'host':'localhost','port':9200}])

e1={
    "first_name":"nitin",
    "last_name":"panwar",
    "age": 27,
    "about": "Love to play cricket",
    "interests": ['sports','music'],
}
print(e1)

res = es.index(index='megacorp',doc_type='employee',id=1,body=e1)

e2={
    "first_name" :  "Jane",
    "last_name" :   "Smith",
    "age" :         32,
    "about" :       "I like to collect rock albums",
    "interests":  [ "music" ]
}
e3={
    "first_name" :  "Douglas",
    "last_name" :   "Fir",
    "age" :         35,
    "about":        "I like to build cabinets",
    "interests":  [ "forestry" ]
}

res=es.index(index='megacorp',doc_type='employee',id=2,body=e2)
res=es.index(index='megacorp',doc_type='employee',id=3,body=e3)
res=es.get(index='megacorp',doc_type='employee',id=3)

# Deleting a document:
res=es.delete(index='megacorp',doc_type='employee',id=3)

res= es.search(index='megacorp',body={'query':{'match_all':{}}})
print('Got %d hits:' %res['hits']['total'])

res= es.search(index='megacorp',body={'query':{}})
print(res['hits']['hits'])

res= es.search(index='megacorp',body={'query':{'match':{'first_name':'nitin'}}})
print(res['hits']['hits'])
