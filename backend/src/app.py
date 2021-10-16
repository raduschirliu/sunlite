import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

load_dotenv()

port = int(os.getenv('PORT', 8000))
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

@app.route('/')
@cross_origin()
def hello_world():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(port=port, threaded=True)