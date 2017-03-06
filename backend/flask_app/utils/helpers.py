from flask import request

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