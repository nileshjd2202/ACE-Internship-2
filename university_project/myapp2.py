import requests
import json

URL = "http://127.0.0.1:8000/collegecreate/"
data = {
    'code': '008',
    'name': 'Government Engineering College Patan',
    'address': 'Patan',
}
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
data = r.json()
print(data)