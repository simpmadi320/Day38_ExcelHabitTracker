import requests
from datetime import datetime

NUTRITION_API_KEY = "1cd51a83a2738764c34f804783c480e7"
NUTRITION_APP_ID = "90d21d2c"

headers = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY
}

END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/98f8b4075ad92eb58c2df0a998a85516/myWorkouts/workouts"

exercise_input = input("What workout did you do? ")

today = datetime.today()
birthday = datetime(2000, 1, 16)
age = (today - birthday).days // 365 #Rounds down to the nearest whole number

exercise_param = {
    "query": exercise_input,
    "weight_kg": 93,
    "height_cm": 172.72,
    "gender": "female",
    "age": age
}

response = requests.post(END_POINT, json=exercise_param, headers=headers)
data = response.json()
#print(data)

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, auth=(
      "msimpson",
      "J@v3rP!9n*",
  ))
#print(sheet_response.text)
print("complete!")
