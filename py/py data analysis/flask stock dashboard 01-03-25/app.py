"""
/data_dashboard  
├── app.py  
├── templates/  
│   ├── index.html  
│   └── dashboard.html  
├── static/  
│   └── plot.png  
└── uploaded.csv
"""
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from pandas import DataFrame, Series
import seaborn as sns
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend


import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    uploaded_file.save('uploaded.csv')
    return redirect(url_for('dashboard'))

@app.route('/dashboard', methods=['GET'])
def dashboard():
    df=pd.read_csv('uploaded.csv')
    plt.figure(figsize=(12, 6))  # Set a larger figure size
    sns.barplot(x='STOCK', y='PRICE', data=df)
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.tight_layout()       # Adjust layout to prevent clipping
    plt.title('Stock prices')
    plt.xlabel('Stock')
    plt.ylabel('Price')
    plt.savefig('static/plot.png')
    return render_template('dashboard.html', df=df)

if __name__ == '__main__':
    app.run(debug=True)
