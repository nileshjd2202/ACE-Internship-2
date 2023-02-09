import requests
import json

URL = "http://127.0.0.1:8000/collegeapi/"


def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}

    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data(2)

def post_data():
    data = {
        'code': '010',
        'name': 'Government Engineering College Modasa',
        'address': 'Modasa'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


post_data()
