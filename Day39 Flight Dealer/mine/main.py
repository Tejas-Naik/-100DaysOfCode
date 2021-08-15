#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from flight_search import FlightSearch
sheet_data_temp = FlightData()
sheet_data = sheet_data_temp.data

iata_code_list = []

for i in range(9):
    iata_code_list.append(sheet_data['prices'][i]['iataCode'])

