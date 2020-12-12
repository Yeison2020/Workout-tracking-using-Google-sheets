import requests
import os
from datetime import datetime


GENDER = "Male"
WEIGHT_KG = NONE
HEIGHT_CM = NONE
AGE = NONE
APP_ID = "NONE"
API_KEY = "NONE"

API_KEY_OS = os.environ(API_KEY)
APP_ID_OS = os.environ(APP_ID)

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheets_end_point = os.environ("https://docs.google.com/spreadsheets/")
exercie_text_input = input("what excercises you did ?\n")



hearder = {"x-app-id": APP_ID_OS, "x-app-key": API_KEY_OS}

parameters = {"query": exercie_text_input, "gender": GENDER, "weight_kg": WEIGHT_KG, "height_cm": HEIGHT_CM, "age":AGE}

response.requests.post(exercise_endpoint, json = parametersl , headers = hearder)

result = response.json()
print(result)

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for excercise in result["excercies"]:
    sheet_inputs = {"workout":
                        {"date": today,
                        "time":now_time,
                        "excercise": excercise["name"].title(),
                        "duration": excercise["duration_min"],
                        "calories": exercise["nf_calories"]}


                    }


sheet_response = requests.post(sheets_end_point, json=sheet_inputs)


sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    auth=(
        os.environ["USERNAME"],
        os.environ["PASSWORD"],
    )
)


bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}
sheet_response = requests.post(
    sheet_endpoint,
    json=sheet_inputs,
    headers=bearer_headers
)

print(sheet_response.text)

