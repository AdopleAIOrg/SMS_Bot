import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hello World 1</h1>'''

@app.route("/receivemsg",  methods = ['POST'])
def recive_message():
    input_msg = request.get_json()    
    print("input_msg", input_msg)
    return jsonify({'success': True, 'message': input_msg['content'] })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)