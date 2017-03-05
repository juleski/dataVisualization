#!flask/bin/python
from flask import Flask, jsonify, make_response, request, send_file

from utils import *
from flask_cors import cross_origin

from middleware.middlewareData import MiddlewareData

app = Flask(__name__)

@app.route('/horangi/api/v1.0/data', methods=['GET'])
@cross_origin(origin='http://localhost:port')
def get_data():
    queryfilter = {
        'size': getParam('size'),
        'openPorts': getListParam('openPorts'),
        'closedPorts': getListParam('closedPorts')
    }
    
    middleware = MiddlewareData()
    data = middleware.get_data(queryfilter)
            
    return jsonify({
        'data': data,
        'status': 'success'
        })

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({
        'error': 'Not found',
        'status': 'failed'
        }), 404)