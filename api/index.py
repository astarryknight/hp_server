import time
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(
 app,
 resources={
  r"/*": {
   "origins": "*",
   "methods": [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
   ],
   "allow_headers": [
    "Content-Type",
    "Authorization",
   ],
  }
 },
)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/time')
def get_current_time():
    return {'time': time.time()}