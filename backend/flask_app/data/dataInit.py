from ..utils.data import *
from ..utils.constants import *
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Index
import os, json, sys


def populate_es_data():
    # Define a default Elasticsearch client
    connections.create_connection(hosts=[ES_HOST])
    if not Index(INDEX).exists():
        Data.init()
        i = 0
        dirToRead = os.getcwd() + '/flask_app/data/nmap_raw/'
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
