import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = '58'
HEIGHT_CM = '172'
AGE = '15'

APP_ID = 'ade4573d'
API_KEY = 'a95c4ed543700fb372f62f5c95874509'

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = 'https://api.sheety.co/7d415d13c97ec10235f431bbbf3f67a5/workoutTracking/workouts'

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
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # #No Auth
    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    #
    #
    # #Basic Auth
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     auth=(
    #         'RNTejas',
    #         'RN_Tejasprogrammer',
    #     )
    # )

    #Bearer Token
    bearer_headers = {
        "Authorization": f"Bearer qwertyuiop1234567890",
        "Content-Type": "application/json",
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)
