import requests
from datetime import datetime
import os

APP_ID = "66d0be62"
API_KEY = "e52cb1d3ba6c2194a05c7037c98f57e8"
sheet_endpoint = "https://docs.google.com/spreadsheets/d/15lVXVCLuKMPNaebeA3aqfqXGlH6dqyPiWTNkkgK_eVk/edit#gid=0"


print(APP_ID)
print(API_KEY)

exe = input("Tell me which exercise you did: ")

exercise_data = {
    "query": exe,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 183,
    "age": 24
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

api = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", data=exercise_data, headers=headers)
result = api.json()
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

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

    print(sheet_response)