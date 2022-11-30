import requests
import json


url = "http://127.0.0.1:8000/diabetes_prediction"

# 3,126,88,41,235,39.3,0.704,27
#3,113,44,13,0,22.4,0.14,22
# 4,110,92,0,0,37.6,0.191,30 out : 0
# 10,168,74,0,0,38,0.537,34
input_dictionary = {
    "Pregnancies": 10,
    "Glucose": 168,
    "BloodPressure": 74,
    "SkinThickness": 0,
    "Insulin": 0,
    "BMI": 38,
    "DiabetesPedigreeFunction": 0.537,
    "Age": 34,
}
print(input_dictionary)
input_json = json.dumps(input_dictionary)

response = requests.post(url=url,data=input_json)
print(response.text)
