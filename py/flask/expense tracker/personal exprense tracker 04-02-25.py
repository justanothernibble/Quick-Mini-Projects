"""

Day 21: Weekly Project
Project: Personal Finance Tracker

Description:

    Develop a web application to track personal finances, including income and expenses.

Key Features:

    User Interface:
        A form to add new transactions (income or expense).
        Display a summary of total income, expenses, and balance.
    Database Integration:
        Use SQLite to store transaction data (amount, category, date, type).
        Allow users to edit and delete transactions.
    Dynamic Reports:
        Generate charts or tables for spending by category or over time.
    Advanced Features (Optional):
        Authentication for multiple users.
        Export data to a CSV file.
"""

from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from matplotlib import pyplot as plt
import os # import os, used for file paths

# Get the absolute path to the script directory
script_dir = os.path.dirname(os.path.abspath(__file__)) # __file__ is the current file
db_path = os.path.join(script_dir, 'finances.db') 

app = Flask(__name__) # creates an instance of the Flask class
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}' # tells the program that the sqlite database being accessed is the path for the current file with the name 'finances.db'
db = SQLAlchemy(app) # create a SQLAlchemy instance

IMAGE_FOLDER = 'static/images'
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

class FinancialEntry(db.Model): # define a FinancialEntry class that inherits from db.Model
    id = db.Column(db.Integer, primary_key=True) # define a column for the id of the transaction
    amount = db.Column(db.Float, nullable=False) # define a column for the amount of the transaction
    category = db.Column(db.String(100), nullable=False) # define a column for the category of the transaction
    date = db.Column(db.Date, nullable=False) # define a column for the date of the transaction
    type = db.Column(db.String(10), nullable=False) # define a column for the type of the transaction (income or expense)

    def __repr__(self): # define a method that returns a string representation of the FinancialEntry object
        return f"FinancialEntry(amount={self.amount}, category={self.category}, date={self.date}, type={self.type})" # for debugging purposes
    
    def addEntry(self): # define a method that adds a new entry to the database
        db.session.add(self) # add the entry to the session
        db.session.commit() # commit the changes

    def deleteEntry(self): # define a method that deletes an entry from the database
        db.session.delete(self) # delete the entry from the session
        db.session.commit() # commit the changes

    def updateEntry(self): # define a method that updates an entry in the database
        db.session.commit() # commit the changes

@app.route('/', methods=['GET']) # route to handle GET requests to the root
def index(): # function to return the index.html template
    entries = FinancialEntry.query.all() # get all entries from the database
    return render_template('index.html', entries=entries) # return the index.html template

@app.route('/add', methods=['GET', 'POST']) # route to handle GET and POST requests to the /add endpoint
def add(): # function to return the add.html template
    if request.method == 'POST': # if the request method is POST
        amount = request.form['amount'] # get the amount from the form
        category = request.form['category'] # get the category from the form
        date_string = request.form['date'] # get the date from the form
        date = datetime.strptime(date_string, '%Y-%m-%d').date() # convert the date string to a date object
        type = request.form['type'] # get the type from the form
        entry = FinancialEntry(amount=amount, category=category, date=date, type=type) # create a new FinancialEntry object
        entry.addEntry() # add the entry to the database
        return redirect(url_for('index')) # redirect to the index page
    return render_template('add.html') # return the add.html template

@app.route('/display', methods=['GET'])
def display():
    # Generate a bar chart of spending by category
    entries = FinancialEntry.query.all()
    if not entries:
        return "No entries found. Add some data first."

    categories = [entry.category for entry in entries]
    amounts = [entry.amount for entry in entries]

    # Debug output
    print("Categories:", categories)
    print("Amounts:", amounts)

    plt.bar(categories, amounts)  # Create a bar chart of spending by category
    plt.xlabel('Category')  # Set the x-axis label
    plt.ylabel('Amount')  # Set the y-axis label
    image_path = os.path.join(IMAGE_FOLDER, 'graph.png')
    plt.savefig(image_path)
    plt.close()

    # Render HTML and pass the image file path
    return render_template('display.html', image_filename='images/graph.png')

@app.route('/delete/<int:id>', methods=['POST']) # route to handle POST requests to the /delete/<id> endpoint
def delete(id): # function to delete an entry from the database
    entry = FinancialEntry.query.get(id) # get the entry from the database
    entry.deleteEntry() # delete the entry from the database
    return redirect(url_for('index')) # redirect to the index page

@app.route('/edit/<int:id>', methods=['GET', 'POST']) # route to handle GET and POST requests to the /edit/<id> endpoint
def edit(id): # function to return the edit.html template
    entry = FinancialEntry.query.get(id) # get the entry from the database
    if request.method == 'POST': # if the request method is POST
        entry.amount = request.form['amount'] # get the amount from the form
        entry.category = request.form['category'] # get the category from the form
        entry.date = request.form['date'] # get the date from the form
        entry.type = request.form['type'] # get the type from the form
        entry.updateEntry() # update the entry in the database
        return redirect(url_for('index')) # redirect to the index page
    return render_template('edit.html', entry=entry) # return the edit.html template

if __name__ == '__main__': # if this file is being run directly
    with app.app_context():
        db.create_all() # create all the tables in the database
    app.run(debug=True) # run the Flask app in debug mode
