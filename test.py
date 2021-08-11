import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "How to get smart", "likes": 456, "views": 554436},
        {"name": "How to create a database", "likes": 66, "views": 110876800},
        {"name": "How to read pdf usin Delphi", "likes": 140, "views": 1145000},
        {"name": "How to create a variable", "likes": 710, "views": 110023450}]

for i in range(len(data)):
    response = requests.get(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
