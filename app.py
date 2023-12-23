import flask
from flask import Flask, request, jsonify
from twilio import twiml

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hello World 2</h1>'''

@app.route("/receivemsg",  methods = ['POST'])
def recive_message():
    input_msg = request.get_json()    
    print("input_msg", input_msg)
    return jsonify({'success': True, 'message': input_msg['content'] })


@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    resp = twiml.Response()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    return str(resp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
