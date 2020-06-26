from json import dumps
from flask import make_response

def jsonify2(status=200, indent=10, sort_keys=True, **kwargs):
  response = make_response(dumps(dict(**kwargs), indent=indent))
  response.headers['Content-Type'] = 'application/json; charset=utf-8'
  response.headers['mimetype'] = 'application/json'
  response.status_code = status
  return response