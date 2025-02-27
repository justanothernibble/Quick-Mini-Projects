# Import the Flask class and the render_template function from the flask module
from flask import Flask, render_template, request

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
        name = request.form['name']
        return render_template("form.html", name = name)
# In order to access Codeium chat on VSC, press ctrl+shift+P and type "Codeium"

# Check if the script is being run directly (and not imported as a module)
if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)


"""'''
    <form action = "/form" method="post">
        <input type="text" name="name" placeholder="Enter your name">
        <button type="submit">Submit</button>
    </form>
    '''"""