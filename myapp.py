"""
FOR TESTING APIS BY CALLING THEM
"""

import json

import requests

# URL = "http://localhost:8080/create_student/"
#
# data = {
#     "name": "Soma",
#     "roll": 1234,
#     "city": "Asn"
# }
#
# json_data = json.dumps(data)
# r = requests.post(url=URL, data=json_data)
#
# data = r.json()
# print(f"create_student data {data}")


URL = "http://localhost:8080/studentapi/"


def get_data(_id=None):
    data = {}
    if _id is not None:
        data = {"id": _id}
        # print(f"Data --> {data}")
    json_data = json.dumps(data)
    # print(f"JSON_DATA --> {json_data}")
    r = requests.get(URL, data=json_data)
    data = r.json()
    print(f"get_data {data}")


# get_data()


def post_data():
    data = {
        "name": "Aroshna",
        "roll": 155,
        "city": "Hydrabad"
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(f"post_data {data}")


post_data()


def update_data():
    # data = {
    #     "id": 8,
    #     "name": "Arup",
    #     # "roll": 111, --- not updating ROLL partial update
    #     "city": "Durgapur"
    # }

    data = {
        "id": 2,
        "name": "Animesh Banerjee",
        "city": "Durgapur"
    }

    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(f"post_data {data}")


# update_data()


def delete_data():
    data = {"id": 8}

    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    # print(f"delete_data {data}")

# delete_data()
