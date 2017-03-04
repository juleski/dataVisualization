from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q, Mapping, DocType, Nested, Object
from elasticsearch_dsl import DocType, Date, Integer, Keyword, Text, Ip
from elasticsearch_dsl.connections import connections


client = Elasticsearch()

s = Search(using=client, index="horangi") \
  .query("match_all")
s._extra['size'] = 4


i = 0
response = s.execute()
for hit in response:
	i += 1
	print hit

print i


