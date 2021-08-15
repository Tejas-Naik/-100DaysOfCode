import requests
from datetime import datetime

# response = requests.get('https://api.sunrise-sunset.org/json?lat=16.425548&lng=74.586954&date=today')

parameter = {
    'lat': 16.425548,
    'lng': 74.586954,
    # the date in the pythonic way
    'formatted': 0,
}

# we can pass dictionaries as parameters!
response = requests.get('https://api.sunrise-sunset.org/json', params=parameter)
response.raise_for_status()
data = response.json()
# print(data)

sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]    # splitting for better formatting
sunset = data['results']['sunset'].split('T')[1].split(':')[0]      # splitting for better formatting
print("Sunrise:", sunrise)
print("Sunset:", sunset)

time_now = datetime.now()
print("Current_hour: ", time_now.hour)




