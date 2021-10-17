import os
import datetime
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from twilio.twiml.messaging_response import MessagingResponse

from .lifx_accessor import start_sunrise

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

    # add info to DB
    start_sunrise() #testing

    # send confirmation
    resp = MessagingResponse()
    resp.message("hello " + from_number)

    return str(resp)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/insert")
def insert_test():
    timestamp = "1999-01-08 04:05:06"

    db.post_event("on", "kelvin:500 saturation:1", 0.75, 5, datetime(timestamp), 1, 1)

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

if __name__ == '__main__':
    app.run(port=port, threaded=True)
