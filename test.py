import requests

BASE = "http://127.0.0.1:5000/"

#response = requests.get(BASE + "profile")

#response = requests.get(BASE + "data")

response = requests.post(BASE + "data", {"location": "Physics Department", "lat": 18.004741066082236, "long": -76.74875280426826, "percentage_full": 56})

#response = requests.post(BASE + "profile", {"username": "coolieman", "role": "Electronics Engineer", "color": "Blue"})

#response = requests.patch(BASE + "data/1", {"location": "Engineering Department", "lat": 16.48526135, "long": 19.1235848})

#response = requests.patch(BASE + "profile", {"username": "Michael", "role": "Biomedical Enigneer", "color": "gray"})

#response = requests.delete(BASE + "data/3")
print(response.json())