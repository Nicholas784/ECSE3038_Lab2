import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "profile", {"username": "Celine", "role": "Nurse", "color": "green"})
print(response.json())