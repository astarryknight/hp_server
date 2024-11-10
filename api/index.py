import time
import os
from dotenv import load_dotenv
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask import request
from flask_cors import CORS

load_dotenv()
api_key = os.getenv("API_KEY")

db = {}

# {email : {outputobj}}

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
    input = "MAKE SURE YOUR RESPONSE IS IN THIS FORMAT: Housing: $___,Meals: $___,Cell Service: $___\nMy budget is 1500. I will be living in California. Please recommend the best budget breakdown for a monthly budget with the following categories: Housing, Meals, and cell service. Give one number, not a range."
    response = model.generate_content(input)
    return response.text

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/send_data', methods=['POST'])
def accept_data():
    data = request.get_json()
    print(data["info"], flush=True)
    #parse data
    db[data["info"]["f_name"]["email"]] = {data["info"]["f_name"]["lname"]}
    #db[data["info"]["f_name"]["email"]]


    print(db["a"], flush=True)
    #send to DB

    #send request to gemini
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    input = "MAKE SURE YOUR RESPONSE IS IN THIS FORMAT: Housing: $___,Meals: $___,Cell Service: $___\nMy budget is "+data["info"]["f_name"]["budget"]+". Please recommend the best budget breakdown for a monthly budget with the following categories: Housing, Meals, and cell service. Give one number, not a range."
    response = model.generate_content(input)
    responses = response.text.split(",")

    #send request to rent for housing
    
    #return data.info.f_name

    db[data["info"]["f_name"]["email"]] = {"budget_breakdown":{"housing":responses[0].split(":")[1], "meals":responses[1].split(":")[1], "SIM":responses[2].split(":")[1]}, "housing":[[0,0], [0,1], [2,1]]} #ADD coordinates for housing
    return jsonify({"good": "you did it"}), 200

@app.route('/get_data/<email>')
def get_data(email):
    return db[email]
    #return jsonify({"a",db[a]}), 200


# input_object = 
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

# output_object = 
# {
#     "budget_breakdown": {
#         "housing": 10,
#         "meals": 10,
#         "SIM": 10
#     },
#     "housing": [[0,0], [1,2] , [3,4]],
#     "SIM": "Mint Mobile",
#     "genai":"abc"
# }
