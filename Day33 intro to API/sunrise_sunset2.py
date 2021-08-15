import requests

parameters = {
    'lat': 16.528030,
    'lng': 74.602982,
    'formatted':0   # this is to format the data to 24 hour format
}
response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
data = response.json()

sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]  # this is splitting the 24 hour time
sunset = data['results']['sunset'].split('T')[1].split(':')[0]  # this is splitting the 24 hour time
print(sunrise)
print(sunset)
