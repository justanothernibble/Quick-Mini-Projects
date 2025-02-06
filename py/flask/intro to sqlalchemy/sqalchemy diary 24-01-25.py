from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import os

# Get the absolute path to the script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'diary.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(app) # create a SQLAlchemy instance

class DiaryEntry(db.Model): # define a DiaryEntry class that inherits from db.Model
    id = db.Column(db.Integer, primary_key=True) # id is the primary key
    title = db.Column(db.String(100), nullable=False) # title is a string with a max length of 100
    content = db.Column(db.Text, nullable=False) # content is text
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp()) # timestamp is the current time

@app.route('/', methods=['GET']) # route to handle GET requests to the root
def diary(): # function to return the diary.html template
    entries = DiaryEntry.query.all() # get all entries from the database
    return render_template('diary.html', entries=entries)

@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit_entry(id):
    entry = db.session.get(DiaryEntry, id)
    if request.method == 'POST':
        entry.title = request.form['title_value']
        entry.content = request.form['content_value']
        db.session.commit()
        return redirect(url_for('diary'))
    return render_template('edit.html', entry=entry)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_entry(id):
    entry = db.session.get(DiaryEntry, id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('diary'))

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        print(f"Request Form Data: {request.form}")  # Debugging form data
        if 'title_value' not in request.form or 'content_value' not in request.form:
            return "Form data is missing keys!", 400
        db.session.add(DiaryEntry(
            title=request.form['title_value'],
            content=request.form['content_value']
        ))
        db.session.commit()
        return redirect(url_for('diary'))
    return render_template('add.html')  # Render the add.html form for GET requests


if __name__ == '__main__':
    with app.app_context(): # create an app context
        # Create the tables in the database
        db.create_all() # create all the tables in the database
    app.run(debug=True) # run the Flask app in debug mode

