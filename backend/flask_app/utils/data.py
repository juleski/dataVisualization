from elasticsearch_dsl import DocType, Nested, Date
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