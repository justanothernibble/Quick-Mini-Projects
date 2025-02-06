# Import the Flask class and the render_template function from the flask module
from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
# Define the function that will be executed when the root URL is accessed
def home():
    # Render and return the 'index.html' template
    return render_template('index.html')

# Check if the script is being run directly (and not imported as a module)
if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
