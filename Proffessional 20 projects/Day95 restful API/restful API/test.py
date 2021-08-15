import requests

BASE = "http://127.0.0.1:5000/"

data  =[
    {"likes":3, "name": "Shiva Tandava", "views": 89},
    {"likes":100, "name": "How to install Python", "views": 5000}
]

for i in range(len(data)):
    response = requests.get(BASE + "video/"+ int(i))
    print(response)
