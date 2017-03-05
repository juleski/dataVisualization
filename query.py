from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q, Mapping, DocType, Nested, Object
from elasticsearch_dsl import DocType, Date, Integer, Keyword, Text, Ip
from elasticsearch_dsl.connections import connections


client = Elasticsearch()

# s = Search(using=client, index="horangi") \
#   .query("match_all")


q = Q('match', **{'tcp__151__state': 'open'})
q2 = Q('match', **{'tcp__443__state': 'open'})
# s = Search(using=client, index="horangi") \
#   .query("nested", path="tcp", query=q)
a = [q, q2]

c = Q('bool', should=a)


s = Search(using=client, index="horangi")
s= s.query("nested", path="tcp", query=c)

# s = Search(using=client, index="horangi") \
#   .query("nested", path="addresses", query=Q('match', **{'addresses.ipv4': '104.79.64.197'}))

# s = Search.from_dict({"query": {"match": {"status.state": "up"}}})
# s.using(client)
s._extra['size'] = 44
#s = s[:]


i = 0
response = s.execute()
print response.to_dict()['hits']['hits'][0]['_source']
#print response.to_dict()
for hit in response:
	i += 1
	print hit.tcp

print i


