import time
import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask
from flask import request
from flask_cors import CORS

load_dotenv()
api_key = os.getenv("API_KEY")
print(api_key)

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
    return api_key

@app.route('/genai/<input>')
def gemini(input):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(input)
    return response.text

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/send_data', methods=['POST'])
def accept_data():
    data = request.json
    #return request.get_json(force=True)
    return 'data received'
