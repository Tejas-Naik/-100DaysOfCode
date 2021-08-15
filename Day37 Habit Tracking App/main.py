import requests
from datetime import datetime

USERNAME = 'rntejas'
TOKEN = 'qwertyuiopasdfghjklzxcvbnm0987654321'

"""Creating User"""
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,  # this is like the API key for you
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# we are commenting the code 'cause we have created an account so we don't want to create again
# response = requests.post(url=pixela_endpoint, json=user_params)        # in user_params we have to use JSON format
# print(response.text)

"""Creating a Graph"""
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id': 'graph1',
    'name': 'Coding Graph',
    'unit': 'hour',
    'type': 'int',
    'color': 'shibafu',
}

"""Headers are the ways to protect our secret parameter like password or API Key """
headers = {
    "X-USER-TOKEN": TOKEN,  # as the documentation we are providing X-USER-TOKEN
}

# I have ran this once so I am not gonna create the same graph again:
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

"""Get the graph go to https://pixe.la/v1/users/rntejas/graphs/graph1.html"""

"""Adding Pixels to graph"""

today = datetime.now()
today = today.strftime("%Y%m%d")
# today = datetime(year=2021, month=2, day=17)

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/graph1'
pixel_config = {
    # We are going to use strftime to format the date
    'date': today,
    'quantity': input("How many hours you coded Today?"),
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

"""Updating the data of yesterday so we can put 4 hours instead of 5"""
# updating_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}'
#
# params_to_update = {
#     'quantity': '4'
# }
#
# response = requests.put(url=updating_endpoint, json=params_to_update, headers=headers)
# print(response.text)

"""Deleting a pixel from the graph"""
# delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}'
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
