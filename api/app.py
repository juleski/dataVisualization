#!flask/bin/python
from flask import Flask, jsonify
from elasticsearch_dsl import DocType, Object, Nested, Date
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['localhost:9200'])

app = Flask(__name__)


class Data(DocType):
    status = Object()
    vendor = Object()
    addresses = Object()    
    tcp = Object()
    datetime = Date()
    hostnames = Nested()

    class Meta:
        index = 'horangi'

@app.route('/')
def index():
    return "Hello, World!"


@app.route('/horangi/api/v1.0/status', methods=['GET'])
def get_tasks():
	res = Data.get(id='AVqZgZwuRETTcytxWd56')
	print type(res.status)
	return jsonify({'item': res.to_dict()})

if __name__ == '__main__':
    app.run(debug=True)