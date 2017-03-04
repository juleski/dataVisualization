from elasticsearch_dsl import DocType, Object, Nested, Date

class Data(DocType):
    status = Object()
    vendor = Object()
    addresses = Object()    
    tcp = Object()
    datetime = Date()
    hostnames = Nested()

    class Meta:
        index = 'horangi'