import requests
from datetime import datetime

NUTRI_APP_ID = ""
NUTRI_API_KEY = ""

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/{UNIQUE_KEY}/workoutTracker/workouts"

exercises = {
    "query": input("What exercises:")
}

headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY
}

data = requests.post(url=EXERCISE_ENDPOINT,
                     json=exercises, headers=headers).json()


for exercise in data["exercises"]:
    # print(exercise)
    json = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().time().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(
        url=SHEETY_ENDPOINT, json=json, auth=("", ""))
    print(response.text)
