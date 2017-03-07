from elasticsearch_dsl import DocType, Nested, Date, Keyword
from constants import *

class Data(DocType):
    status = Nested()
    vendor = Nested()
    addresses = Nested()    
    tcp = Nested()
    datetime = Date()
    hostnames = Nested()

    class Meta:
        index = INDEX

class Port(DocType):
	name = Keyword()
	date = Date()

	class Meta:
		index = INDEX