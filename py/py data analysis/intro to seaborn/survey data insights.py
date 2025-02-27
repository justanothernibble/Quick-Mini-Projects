"""
Seaborn is like matplotlib but on steroids."""

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import pandas as pd

import os
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
os.chdir(script_dir)

df = pd.read_csv('survey.csv')
df.head()
print(df)

"""tips = sns.load_dataset('tips')"""


sns.boxplot(x='Gender', y='Income', data=df)
sns.set_style('whitegrid')
sns.set_palette('pastel')
sns.set_context('poster')
plt.title("Relationship between gender and income")
plt.show()


# Heatmap for numeric columns
corr = df.corr(numeric_only=True)
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Survey Correlation Heatmap')
plt.show()


sns.lineplot(x='Age', y='Income', hue='Gender', data=df)
plt.title('Relationship between age and income')
plt.show()
