import os
import datetime
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS, cross_origin
from twilio.twiml.messaging_response import MessagingResponse

from .auth import verify_jwt

# Load dotenv files
load_dotenv()

# Initialize DB tables
from .util import db
db.create_event_table()
db.create_users_table()

# Initialize Flask
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

    try:
        # Get the api_key associated with the from_number
        api_key = db.get_user_api_key(from_number)

        if api_key is None:
            response = "We could not find a user associated with your phone number. Please sign up at sun-lite.netlify.com."
        else:
            scheduled_at = None

            # convert the body to a datetime
            time_from_body = datetime.datetime.strptime(body, "%H:%M").time()

            now = datetime.datetime.today()
            scheduled_today = datetime.datetime.combine(now.date(), time_from_body)

            # if date.now is greater than the provided time, then increment to tomorrow
            if  scheduled_today < now:
                scheduled_at = scheduled_today
            else:
                tomorrow = datetime.date.today() + datetime.timedelta(days=1)
                scheduled_at = datetime.datetime.combine(tomorrow, time_from_body)

            db.post_event(scheduled_at, api_key)

            response = "Sunrise scheduled :)"
    except (Exception):
        response = "Unknown command, usage: <HH:MM>"

    finally:
        # send confirmation
        resp = MessagingResponse()
        resp.message(response)

        return str(resp)

@app.route("/")
def index():
    return "MMPP MHacks-14 Heroku App is running!"

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
