import datetime as dt
import requests
import os

APP_ID = os.environ.get("APP_ID")
WORKOUT_API_KEY = os.environ.get("WORKOUT_API_KEY")
SHEET_TOKEN = os.environ.get("SHEET_TOKEN")
WEIGHT = os.environ.get("WEIGHT")
HEIGHT = os.environ.get("HEIGHT")
AGE = os.environ.get("AGE")


nutritionix_endpoint = os.environ.get("nutritionix_endpoint")
sheet_endpoint = os.environ.get("sheet_endpoint")

workout_auth_header = {
    "x-app-id": APP_ID,
    "x-app-key": WORKOUT_API_KEY,
}

query = input("Workout: \n")

workout_params = {
    "query": query,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
workout_response = requests.post(url=nutritionix_endpoint, json=workout_params, headers=workout_auth_header)
print(workout_response.raise_for_status())
result = workout_response.json()
print(result)

calories = result["exercises"][0]["nf_calories"]
exercise = result["exercises"][0]["name"]
formatted_exercise = exercise.title()
duration = result["exercises"][0]["duration_min"]

sheet_auth_header = {
    "Authorization": SHEET_TOKEN
}
today_date = dt.datetime.now()
formatted_date = today_date.strftime('%d/%m/%Y')

current_time = dt.datetime.now()
formatted_time = current_time.strftime('%H:%M:%S')

sheet_params = {
    "workout": {
        "date": formatted_date,
        "time": formatted_time,
        "exercise": formatted_exercise,
        "duration": duration,
        "calories": calories,
    }
}

sheet_response = requests.post(url=sheet_endpoint, json=sheet_params, headers=sheet_auth_header)
print(sheet_response.json())
print(sheet_response.text)
print("Data uploaded")
