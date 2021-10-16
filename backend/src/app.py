import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from twilio.twiml.messaging_response import MessagingResponse
from .lifx_accessor import test_lamp

load_dotenv()

port = int(os.getenv('PORT', 8000))
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

@app.route("/sms", methods=['POST'])
@cross_origin()
def sms_receive():
    # Use this data in your application logic
    from_number = request.form['From']
    to_number = request.form['To']
    body = request.form['Body']

    # add info to DB
    test_lamp() #testing

    # send confirmation
    resp = MessagingResponse()
    resp.message("hello " + from_number)

    return str(resp)


if __name__ == '__main__':
    app.run(port=port, threaded=True)


