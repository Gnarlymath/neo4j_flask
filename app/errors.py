from app import app

@app.errorhandler(404)
def not_found_error(error):
    return "404 baby, that site is absolutely not found"

@app.errorhandler(500)
def internal_error(error):
    return "Error 500, that's something on our end. Sorry"

@app.errorhandler(405)
def request_type_error(error):
    return "405 wrong request type"