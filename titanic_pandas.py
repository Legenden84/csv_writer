import pandas as pd

temp_csv = []

# Creating custom headers
col_names = ['Id', 'Survived', 'Passenger Class', 'Full Name', 'Gender', 'Age', 'SibSp', 'Parch',
             'Ticket number', 'Price', 'Cabin', 'Station']

# Importing data
titanic_data = pd.read_csv('datasets/titanic_pandas.csv', names=col_names, skiprows=[0])
titanic_data = titanic_data[['Id', 'Survived', 'Full Name']]

titanic_data = titanic_data[titanic_data['Survived'] > 0]

print(titanic_data)


