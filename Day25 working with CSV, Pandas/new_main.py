import pandas as pd
import csv

"""
# reading CSV file 
csv_file = pandas.read_csv('data.csv')


# structure of a DataFrame
df = pandas.DataFrame(
    {
        'names': ['Tejas', 'Angela', 'Aaron', 'Qazi'],
        'age': [15, 35, 24, 25],
        'salary': [100, 1000, 300, 4000],
    }
)
print(df['age'])    # if you wanna get the particular column/series
"""

"""
# using csv module to read CSV file
with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temparatures = []

    for row in data:
        if row[1] != 'temp':
            temparatures.append(int(row[1]))
print(temparatures)
"""

weather_data = pd.read_csv('weather_data.csv')
print(weather_data)             # DataFrame type
# printing only temperature out of the df
print(weather_data['temp'])     # series type

# converting csv to dict
data_dict = weather_data.to_dict()      # you can convert dataframe to dictionary
print(data_dict)

# you can convert series to list
temp_list = weather_data['temp'].to_list()
print(temp_list)

# average of temperatures
temps = []
for temp in temp_list:
    temps.append(temp)
average = sum(temps) / len(temps)
print("Pythonic Average:", average)
average_pandas = weather_data['temp'].mean()
print("Pandas avarage:", average_pandas)

# maximum of temperatures
max_temp = weather_data['temp'].max()
print(max_temp)

# minimum of temperatures
min_temp = weather_data['temp'].min()
print(min_temp)

# getting data from columns
# here you have to be careful about the strings and other stuff but you can use the other method
# weather_data['condition']

# column other method
print(weather_data.condition)

# getting data from row
# structure = data[data.day or data['day'] == 'day you want']
monday_row = weather_data[weather_data.day == 'Monday']
print(monday_row)

max_temp_of_week = weather_data[weather_data.temp == weather_data.temp.max()]
print(max_temp_of_week)

# getting particular column from the row (0°C × 9/5) + 32
temp_fahrenhiet = (monday_row.temp * 9/5) + 32
print(temp_fahrenhiet)

# creating a dataframe from scratch
data_ex_dict = {
    'name': ['Tejas', 'Tim', 'Jonas'],
    'scores': [56, 93, 54]
}

data_frame = pd.DataFrame(data_ex_dict)
print(data_frame)

data_frame.to_csv('dataframe.csv')
