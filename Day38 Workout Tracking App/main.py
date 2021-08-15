import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

GENDER = "male"
WEIGHT_KG = '58'
HEIGHT_CM = '172'
AGE = '15'

APP_ID = 'ade4573d'
API_KEY = 'a95c4ed543700fb372f62f5c95874509'

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print(result)

sheety_endpoint = 'https://api.sheety.co/7d415d13c97ec10235f431bbbf3f67a5/workoutTracking/workouts'
response = requests.get(url=sheety_endpoint)
# print(response.json())

sheety_endpoint = 'https://api.sheety.co/7d415d13c97ec10235f431bbbf3f67a5/workoutTracking/workouts'
today = datetime.now()
# parameter_to_upload = {
#     'Date': {
#         'Date': today.strftime('%D/%m/%Y')
#     },
#     'Time': {
#         'Time': today.strftime('%H:%M:%S')
#     },
#     'Exercise': {
#         'Exercise': result['exercises'][0]['name']
#     },
#     'Duration': {
#         'Duration': result['exercises'][0]['duration_min']
#     },
#     'Calories': {
#         'Calories': result['exercises'][0]['nf_calories']
#     }
#
# }

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today.strftime('%D/%m/%Y'),
            "time": today.strftime('%H%M%S'),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    headers = {
        "Authorization: Basic Uk5UZWphczpSTl9UZWphc3Byb2dyYW1tZXI=",
    }

    post_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=headers)
    print(post_response)

    #Basic Authentication
    sheet_response = requests.post(
      sheety_endpoint,
      json=sheet_inputs,
      auth=(
          'RNTejas',
          'RN_Tejasprogrammer',
      )
    )
    print(sheet_response)