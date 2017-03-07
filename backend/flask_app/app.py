#!flask/bin/python
from flask import Flask, jsonify, make_response, request, send_file
from flask_cors import cross_origin
from utils.helpers import *
from utils.constants import *
from dao.dataEsDao import *
from midlayer.dataMidlayer import *

app = Flask(__name__)

@app.route('/exam/api/v1.0/data', methods=['GET'])
@cross_origin(origin='http://localhost:port')
def get_data():
    queryfilter = {
        'size': getParam('size'),
        'openPorts': getListParam('openPorts')
    }
    
    midlayer = DataMidlayer(DataEsDao)
    data = midlayer.get_data(queryfilter)
            
    return jsonify({
        'data': data,
        'status': 'success'
        })

@app.route('/exam/api/v1.0/port', methods=['GET'])
@cross_origin(origin='http://localhost:port')
def get_ports():

    midlayer = DataMidlayer(DataEsDao)
    data = midlayer.get_ports()

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