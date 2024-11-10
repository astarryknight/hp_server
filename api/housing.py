#import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace this with your RentCast API key
RENTCAST_API_KEY = 'RENTCAST'

@app.route('/api/housing', methods=['GET'])
def get_housing_recommendations():
    lat = 30#request.args.get('lat')
    lng = 170#request.args.get('lng')
    radius = request.args.get('radius', 5)  # Default radius is 5 miles if not provided

    # Validate that latitude and longitude are provided
    if not lat or not lng:
        return jsonify({"error": "Latitude and longitude are required"}), 400

    # RentCast API endpoint to search properties by geographic area (latitude, longitude, and radius)
    rentcast_api_url = f'https://api.rentcast.io/v1/listings/rental/long-term?latitude={lat}&longitude={lng}&radius={radius}'

    headers = {
        'Accept': 'application/json',
        'X-Api-Key': 'RENTCAST',
    }

    try:
        # Fetch data from RentCast API
        response = requests.get(rentcast_api_url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        housing_data = response.json()  # Assuming JSON response
        return jsonify(housing_data)

    except requests.exceptions.RequestException as e:
        # Handle any errors with the RentCast API request
        return jsonify({"error": str(e)}), 500
