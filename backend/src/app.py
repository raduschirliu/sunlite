import os
import datetime
import psycopg2
import json
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from twilio.twiml.messaging_response import MessagingResponse

from .lifx_accessor import start_sunrise, disco
from .auth import verify_jwt

# Load dotenv files
load_dotenv()

# Init DB tables
from .util import db
db.create_event_table()
db.create_users_table()

# Init Flask
port = int(os.getenv('PORT', 8000))
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

# Webhook callback from Twilio
@app.route("/sms", methods=['POST'])
@cross_origin()
def sms_receive():
    # Use this data in your application logic
    from_number = request.form['From']
    to_number = request.form['To']
    body = request.form['Body']

    if body == "disco": 
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

@app.route("/insert")
def insert_test():
    timestamp = "1999-01-08 04:05:06"

    db.post_event("on", "kelvin:500 saturation:1", 0.75, 5, datetime(timestamp), 1, 1)

    return "hello"

@app.route("/tests")
def get_tests():
    sql = "SELECT * FROM test"
    db.cursor.execute(sql)

    return "Inserted!"

@app.route("/test/insert")
def test_insert():
    print("wtf?")
    try:
        DATABASE_URL = os.getenv("DATABASE_URL")
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')

        cursor = conn.cursor()

        sql = """INSERT INTO test ("Name") VALUES (%s);"""
        val = ('Hi Jordan!',)
        cursor.execute(sql, val)
        conn.commit()

        # commit the changes
        conn.close()
        print("did the thing")
        return "worked"
    except (Exception, psycopg2.DatabaseError) as error:
        return str(error)
        print(error)

# Update user account information
@app.route('/account', methods=['POST'])
@cross_origin()
def update_account():
    jwt = verify_jwt()

    if jwt == False:
        return "Unauthorized", 401

    print(jwt)
    data = request.json

    if "api_key" not in data or "phone_number" not in data:
        return "Invalid request", 400

    id = jwt["sub"]
    db.update_user_details(id, data["api_key"], data["phone_number"])

    return {
        "id": id,
        "api_key": data["api_key"],
        "phone_number": data["phone_number"]
    }

# Run Flask app
if __name__ == '__main__':
    app.run(port=port, threaded=True)
