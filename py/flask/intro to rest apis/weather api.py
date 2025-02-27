from flask import Flask, jsonify, request # this imports flask (python backend web framework) and jsonify (concerts python data into JSON)

app = Flask(__name__) # creates an instance of flask

weather_data = { # dummy 2D dictionary data
    "tokyo": {"temperature": 22, "conditions": "Sunny"},
    "paris": {"temperature": 15, "conditions": "Rainy"}
}


@app.route('/weather/<city>', methods=['GET']) # if weather/(any city) is accessed, it passes the city into the get_weather(city) function
def get_weather(city): # once the city reaches the function (which is called by app.route etc.), the function is EXCECUTED
    city = city.lower() # this makes the city lowercase in order to ensure data concistency and prevent unwanted errors
    if city in weather_data: # checks if the city is in the dictionary
        return jsonify(weather_data[city]) # if it is, then return the weather data of that specific cityy
    else: # or else,..
        return jsonify({"Error": "City not found"}), 404 # if the city is not found, then return a dictionary of "Error, city not foundE". I do not know what 404 is for

@app.route('/weather', methods=['POST']) # the function is executed if /weather is accessed. also, data is being sent to the server for this.
def add_weather(): # function to add weather to JSON
    new_data = request.get_json() # get JSON data from the request body
    city = new_data['city'].lower()
    weather_data[city] = {
        "temperature": new_data["temperature"],
        "conditions": new_data["conditions"]
    }
    return jsonify({"message": "City added"}), 201  # 201 = Created


if __name__ == '__main__': # if the file is ran as a script and not imported, then run the app
    app.run(debug=True)