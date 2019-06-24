from app import app

@app.route('/response', methods=['GET'])
def response():
    return "good news everyone"

@app.route('/index', methods=['GET'])
def index():
    return "this in the index url"