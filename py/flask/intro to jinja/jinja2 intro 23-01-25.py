# Import the Flask class and the render_template function from the flask module
from flask import Flask, render_template, request

addblogs = [
            { # taken from my cv ;)
            
            'author': "josh",

            'p1Name': "Loan Risk Management System",
            'p1Points': ['Built a comprehensive loan risk management application, incorporating machine learning and data analysis algorithms to assess loan repayment likelihood using Python.',
                    'Enabled streamlined prediction of loan repayment and suggested interest rates based on user data, integrating Logistic Regression and K-NN algorithms for decision-making.',
                    'Constructed an intuitive GUI using PyQt6 for data input and graphical comparisons across customer demographics.'],
            
            'p2Name': "Iris Higgs Boson Hunting",
            'p2Points': ['Led a team of 5students to conduct a research project to investigate methods for estimating the Higgs Boson mass, analysing over 3+ million events from the ATLAS detector at the Large Hadron Collider', 
                        'Developed statistical models to analyse Higgs decay channels, leveraging data science techniques to filter background noise and refine signal detection'],
            
            }
        
        ,

            { # dummy data
            
            'author': 'adam',

            'p1Name': "Machine Learning with Python",
            'p1Points': ['Developed a machine learning model to predict house prices based on attributes such as the number of bedrooms and location.',
                    'Used scikit-learn library to perform data preprocessing, feature engineering, training and testing of the model.'],
            
            'p2Name': "Web Development with Flask",
            'p2Points': ['Created a web application using Flask to display a list of books.',
                    'Used Bootstrap to style the application and SQLite to store the data.'],
            
            }

]



app = Flask(__name__) # Create an instance of the Flask class

@app.route('/') # Define a route for the root URL ('/')
def home(): # Define the function that will be executed when the root URL is accessed
    return render_template('index2.html') # Render and return the 'index2.html' template

@app.route('/blog', methods = ['POST']) # Define a route for the '/blog' URL
def blog(): # Define the function that will be executed when the '/blog' URL is accessed
    if request.method == 'POST': # Check if the request method is POST
        uname = request.form['uname'] # Get the value of the 'uname' form field
        return render_template("child.html", uname = uname, blogs = addblogs) # Render and return the 'blog.html' template

if __name__ == '__main__': # Check if the script is being run directly (and not imported as a module)
    # Run the Flask application in debug mode
    app.run(debug=True) # Run the Flask application in debug mode
