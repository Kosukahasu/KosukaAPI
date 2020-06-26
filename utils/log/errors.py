from utils.json import jsonify2

def error(code, message):
    return jsonify2(indent=8, code=code, error=message)
