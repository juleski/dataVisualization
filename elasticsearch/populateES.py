from Data import *
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Index
import os, json

# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost:9200'])

if not Index('horangi').exists():
    Data.init()
    i = 0
    dirToRead = os.getcwd() + '/nmap_raw/'
    for filename in os.listdir(dirToRead):
        with open(dirToRead + filename, 'r') as f:
            for line in f:
                info = json.loads(line)
                keys = info.keys()
                data = Data()
                if 'status' in keys:
                    data.status=info['status']
                if 'vendor' in keys:
                    data.vendor=info['vendor']
                if 'addresses' in keys:
                    data.addresses=info['addresses']
                if 'tcp' in keys:
                    data.tcp=info['tcp']
                if 'datetime' in keys:
                    data.datetime=info['datetime']
                if 'hostnames' in keys:
                    data.hostnames=info['hostnames']

                data.save()
                i += 1
    print 'Indexed %d files!' % (i)
else:
    print 'DATA ALREADY IN ES'
