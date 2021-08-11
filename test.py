import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "video/1", {"name":"nutela", "likes":10, "views": 11000})
print(response.json())
input()
response = requests.post(BASE + f"video/1")
print(response.json())
