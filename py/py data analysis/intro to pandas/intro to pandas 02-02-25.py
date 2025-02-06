"""df.head() # returns the first 5 rows of the data
df.tail() # returns the last 5 rows of the data
df.sample() # returns a random row of the data
df.sample(3) # returns 3 random rows of the data
df.describe() # returns a summary of the data
df.info() # returns information about the data
df.columns # returns the column names of the data
df.index # returns the index of the data
df.dtypes # returns the data types of the data
df.isnull().sum() # returns the number of missing values in each column of the data
df.isna().sum() # returns the number of missing values in each column of the data
df.duplicated().sum() # returns the number of duplicate rows in the data
df.nunique() # returns the number of unique values in each column of the data
df.corr() # returns the correlation matrix of the data
df.corr().to_csv('correlation_matrix.csv') # saves the correlation matrix to a CSV file"""

import pandas as pd
from pandas import DataFrame as df
from pandas import Series as ser
import os
# Set the default file directory to the one that the script is in
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

data = pd.read_csv('dummy.csv')
desc = data.describe()
print("=====Summary=====")
print(f"Amount of students: {len(data)}")
print(f"Average score: {desc['Score']['mean']:.2f}")
print(f"Minimum score: {desc['Score']['min']}")
print(f"Maximum score: {desc['Score']['max']}")
print(f"Standard Deviation: {(desc['Score']['std']):.2f}")
print(f"Variance: {(desc['Score']['std']**2):.2f}")

passed = data[data['Score'] >= 50]
print(f"Number of students who passed: {len(passed)}")
import matplotlib.pyplot as plt

column_to_plot = input("Enter column to visualize: ")
data[column_to_plot].hist()
plt.title(f'Histogram of {column_to_plot}')
plt.xlabel(column_to_plot)
plt.ylabel('Frequency')
plt.show()
