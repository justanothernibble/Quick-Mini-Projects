# Import the necessary libraries
from flask import Flask, jsonify, redirect, request, render_template  # Importing Flask and jsonify to create a web server and return JSON data
import requests  # Importing the requests library to make HTTP requests to the OpenWeather API
import os

# Create a Flask app instance
app = Flask(__name__)

# Your OpenWeather API key - you can get one for free at https://openweathermap.org/
API_KEY = "YOU'RE NOT GETTING MY API BUDDY"

# The base URL for the OpenWeather API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# This route is for getting the weather data for a given city
@app.route('/api/weather', methods=['GET'])
def get_weather():
    # Get the city name from the query parameter (e.g., /api/weather?city=New+York)
    city = request.args.get('city')

    # If no city is provided, return an error
    if not city:
        return jsonify({"error": "City name is required"}), 400

    # Construct the URL to fetch weather data from the OpenWeather API
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"  # "units=metric" to get temperatures in Celsius

    try:
        # Send the GET request to the OpenWeather API
        response = requests.get(url)

        # Parse the response as JSON
        data = response.json()

        # Check if the city was found
        if response.status_code != 200:
            # Return an error if the city was not found
            return jsonify({"error": data.get("message", "Error fetching weather data")}), 400

        # Extract desired weather information
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }

        # Return the weather data as JSON
        return jsonify(weather_info)

    except requests.exceptions.RequestException as e:
        # Return an error if something goes wrong with the API request
        return jsonify({"error": str(e)}), 500


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form.get('city_value').lower()  # Get city from form
        api_key = API_KEY  # Use the API key from the top of the file
        response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
        weather_data = response.json()  # Parse the JSON response
        return render_template('index.html', weather_data=weather_data)
    return render_template('index.html')  # Render the form for GET requests


if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)
