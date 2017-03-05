#!flask/bin/python
from flask import Flask, jsonify, make_response, request
from elasticsearch_dsl import DocType, Object, Nested, Date, Q, Search
from elasticsearch_dsl.connections import connections
from elasticsearch import Elasticsearch
from utils.resources import Data, getParam, getListParam

from middleware.middlewareData import MiddlewareData

connections.create_connection(hosts=['localhost:9200'])

app = Flask(__name__)


@app.route('/horangi/api/v1.0/data', methods=['GET'])
def get_data():
    queryfilter = {
        'size': getParam('size'),
        'openPorts': getListParam('openPorts'),
        'closedPorts': getListParam('closedPorts')
    }
    
    middleware = MiddlewareData()
    data = middleware.get_data(queryfilter)
            
    return jsonify({
        'result': data,
        'status': 'success'
        })

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({
        'error': 'Not found',
        'status': 'failed'
        }), 404)