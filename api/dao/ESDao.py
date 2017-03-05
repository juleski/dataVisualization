from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q


class ESDao():

	def search(self, queryFilter):
		client = Elasticsearch()
		s = Search(using=client, index='horangi')
		queryList = []

		if (queryFilter['openPorts']):
			for port in queryFilter['openPorts']:
				queryList.append(Q('match', **{'tcp.'+port+'.state': 'open'}))

			query = Q('bool', should=queryList)
			s = s.query('nested', path="tcp", query=query)

		if (queryFilter['size']):
			s._extra['size'] = queryFilter['size']
		else:
			s._extra['size'] = 50

		return s.execute()

