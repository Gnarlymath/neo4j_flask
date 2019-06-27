from app import app
from flask import make_response, jsonify


err404 = {"404":"aw yeah, that site is absolutely not found"}
err405 = {"405":" Wrong request type amigo"}
err500 = {"500":" that is something wrong on our end, sorry!"}

@app.errorhandler(404)
def not_found_error(error):
    return make_response(jsonify(err404), 404)

@app.errorhandler(405)
def request_type_error(error):
    return make_response(jsonify(err405),405)

@app.errorhandler(500)
def internal_error(error):
    return make_response(jsonify(err500),500)

