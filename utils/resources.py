from elasticsearch_dsl import DocType, Nested, Date
from flask import request

class Data(DocType):
    status = Nested()
    vendor = Nested()
    addresses = Nested()    
    tcp = Nested()
    datetime = Date()
    hostnames = Nested()

    class Meta:
        index = 'horangi'


def getParam(key):
    param = request.args.get(key)
    if param:
        return param
    else:
        return None

def getListParam(key):
    param = request.args.get(key)
    if param:
        return list(set(param.split(',')))
    else:
        return None