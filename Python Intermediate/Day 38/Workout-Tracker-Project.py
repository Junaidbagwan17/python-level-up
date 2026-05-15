from google import genai
import requests
from datetime import datetime

# API key automatically comes from GEMINI_API_KEY
client = genai.Client(api_key="YOUR API KEY")

user_input = input("Tell me about your workout: ")

prompt = f"""
You are a fitness data extractor.
Analyze this: "{user_input}"

Return ONLY a comma-separated list for each exercise.
Format: Exercise, Duration (min), Calories

Example:
Running, 30, 300
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

today_workout = response.text.split("\n")
# -----------------------------------------------------------------------------

# open sheety get login with same opend file to that app and then get api key
SHEETY_Endpoint = "https://api.sheety.co/YOUR API KEY/workoutTracking/workouts"

# 2. Get Current Date and Time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for workout  in today_workout:
    data = workout.split(",")
    worksheet_columns = {
        "workout": {
            "date":today_date,
            "time":now_time,
            "exercise":today_workout[0],
            "duration":today_workout[1],
            "calories":today_workout[2]
        }
    }

    sheety_response = requests.post(url=SHEETY_Endpoint, json=worksheet_columns)
    print(sheety_response.text)
