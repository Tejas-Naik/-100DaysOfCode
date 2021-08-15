from twilio.rest import Client
import os
import requests

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
API_KEY = 'f2fcabee8b0ed9c496b71b47f76e8b82'
account_sid = 'AC39c3ede5fa16c25b8159996f0450c631'
auth_token = '2a9d442fb1e127bdc0e8cf5c6f124542'

weather_parameters = {
    'lat': 16.528030,
    'lon': 74.602982,
    'appid': API_KEY,
    'exclude':'daily,minutely,current,alerts'
}
response = requests.get(OWM_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()

# weather_slice = weather_data['hourly'][:12]
# weather_slice_data = weather_slice[0]['weather'][0]['id']
# print(weather_slice_data)

will_rain = False

for i in range(12):
    if response.json()['hourly'][i]['weather'][i]['id'] < 700:
        will_rain = True
        break
    else:
        print("Not Rain")
        break

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Today is gonna rain don't forget to bring an Umbrella☔.",
                        from_='+12013836197',
                        to='+9181039620'
                    )
    print(message.status)