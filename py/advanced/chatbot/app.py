import bot
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from flask import Flask, render_template, request, jsonify


# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')

# Define the function that will be executed when the root URL is accessed
def home():
    # Render and return the 'index.html' template
    return render_template('index.html')

@app.route('/form', methods = ['POST'])
def form():
    if request.method == 'POST':
        inputted_string = request.form['input_box']
        bot.generate_response(inputted_string)
        print(bot.string_list)
        print(bot.response_list)
        return render_template("form.html", string_list=bot.string_list, response_list=bot.response_list )

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
