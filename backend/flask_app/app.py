from flask import Flask, Blueprint, jsonify, make_response, request, send_file
from flask_cors import cross_origin
from utils.helpers import *
from utils.constants import *
from dao.dataEsDao import *
from midlayer.dataMidlayer import *

appBlueprint = Blueprint('exam_api', __name__)

@appBlueprint.route('/data', methods=['GET'])
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

@appBlueprint.route('/port', methods=['GET'])
@cross_origin(origin='http://localhost:port')
def get_ports():

    midlayer = DataMidlayer(DataEsDao)
    data = midlayer.get_ports()

    return jsonify({
        'data': data,
        'status': 'success'
        })

@appBlueprint.errorhandler(404)
def not_found(error):
    return make_response(jsonify({
        'error': 'Not found',
        'status': 'failed'
        }), 404)