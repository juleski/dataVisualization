from ..utils.data import *
from ..utils.constants import *
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Index
from datetime import datetime
import os, json, sys



def populate_es_data():
    # Define a default Elasticsearch client
    connections.create_connection(hosts=[ES_HOST])
    if not Index(INDEX).exists():
        Data.init()
        Port.init()
        i = 0
        ports = []
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
                        for port in info['tcp']:
                            ports.append(port)
                    if 'datetime' in keys:
                        data.datetime=info['datetime']
                    if 'hostnames' in keys:
                        data.hostnames=info['hostnames']

                    data.save()
                    i += 1
        print 'Indexed %d files!' % (i)
        i = 0
        ports = list(set(ports))
        for port in ports:
            i += 1
            portType = Port()
            portType.name = port
            portType.date = datetime.now()
            portType.save()
        print 'Indexed %d ports!' % (i)

    else:
        print 'DATA ALREADY IN ES'
