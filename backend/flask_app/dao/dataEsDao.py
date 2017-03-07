from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q
from ..utils.constants import *
import os


class DataEsDao():

	def search(self, queryFilter):
		client = Elasticsearch([ES_HOST])
		s = Search(using=client, index=INDEX)
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

		s = s.sort('datetime')

		return s.execute()

	def get_ports(self):
		client = Elasticsearch([ES_HOST])
		s = Search(using=client, index=INDEX)
		s= s.query("type", value='port')
		s._extra['size'] = 50
		return s.execute()

