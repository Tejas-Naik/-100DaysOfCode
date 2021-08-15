# with open('weather_data.csv') as data_files:
#     data = data_files.readlines()
#     print(data)

# better way to read CSV files
# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#         # print(row)
# print(temperatures)
# Documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html
import pandas

data = pandas.read_csv('weather_data.csv')
temperatures = data['temp']
conditions = data['condition']
print(temperatures)
print(conditions)

print(data)

# there are two main data structures in Pandas they are ##DataFrames, ##Series

data_dict = data.to_dict()
print(data_dict)