import requests
from twilio.rest import Client

# Twillio recovery code "AZ-GC3DphGOJ9zH_ATkGmiK03belBZ4GW0-M9ndh"
# Twilio credentials
API_KEY = 'f2fcabee8b0ed9c496b71b47f76e8b82'
ACCOUNT_SID = 'AC39c3ede5fa16c25b8159996f0450c631'
AUTH_TOKEN = '2a9d442fb1e127bdc0e8cf5c6f124542'

weather_parameters = {
    'lat': 16.529582,
    'lon': 74.602776,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily',
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

# weather_slice = weather_data['hourly'][:12]
# for hour_data in weather_slice:
#     condition_code = hour_data['weather'][0]['id']
#     if condition_code < 700:
#         print("Bring an umbrella")

will_rain = False

for i in range(12):
    if weather_data['hourly'][i]['weather'][0]['id'] > 700:
        will_rain = True
        break
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="Hey there this is Pythonic weather Bot built by RN Tejas. today is gonna rain so don't forget to bring an umbrella☔, See you next time!",
        from_='+12013836197',
        to='+916362881692'
    )
    print(message.status)
