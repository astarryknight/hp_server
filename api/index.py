import time
import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask
from flask import request
from flask_cors import CORS

load_dotenv()
api_key = os.getenv("API_KEY")

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
    return "hwllo world"

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


# object = 
# {
#     "info" : {
#         "f_name": "John",
#         "l_name": "Doe",
#         "email": "example@domain.com",
#         "pasword": "1234"
#     },
#     "resources": {
#         "budget": 1000,
#         "time": 6,
#         "location": [0.1, 0.1]
# }}
