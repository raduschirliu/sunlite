import os
import json
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from twilio.twiml.messaging_response import MessagingResponse

from .lifx_accessor import start_sunrise, disco
from .auth import verify_jwt

load_dotenv()

from .util import db
db.create_event_table()

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

    if(body == "disco"): 
        disco()
        response = "DISCO ON!"
    else: 
        # check if phone number is registered
        # update database
        response = "Sunrise scheduled :)"
        start_sunrise() #testing

    # send confirmation
    resp = MessagingResponse()
    resp.message(response)

    return str(resp)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/tests")
def get_tests():
    sql = "SELECT * FROM test"
    db.cursor.execute(sql)

    rows = db.cursor.fetchall()

    text = ""
    for row in rows:
        text += str(row)

    return text

@app.route('/account', methods=['POST'])
@cross_origin()
def update_account():
    jwt = verify_jwt()

    if jwt == False:
        return "oeh noe :("

    print(jwt)
    data = request.json

    if "api_key" not in data or "phone_number" not in data:
        return "invalid data"

    id = jwt["sub"]
    db.update_user_details(id, data["api_key"], data["phone_number"])

    return "Ok"

if __name__ == '__main__':
    app.run(port=port, threaded=True)
