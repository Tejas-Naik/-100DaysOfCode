import requests
from datetime import datetime

# pixela credentials
USERNAME = 'rntejas'
TOKEN = 'qwertyuiopasdfghjklzxcvbnm0987654321'
pixela_endpoint = 'https://pixe.la/v1/users'

# parameters for ctreating user
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'   # not really
}

# we can comment the following code because we have created an user and we don't want to create again
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

# graph 
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_params = {
    'id': 'graph2',
    'name': 'Workout Tracking',
    'unit': 'minutes',
    'type': 'float',
    'color': 'shibafu'      # green color
}

graph_header = {
    'X-USER-TOKEN': TOKEN
}

graph_response = requests.post(graph_endpoint, json=graph_params, headers=graph_header)

# adding pixel to the graph
adding_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/graph2'

now = datetime.now()
formatted_date = now.strftime("%Y%m%d")

pixel_params = {
    'date': formatted_date,
    'quantity': input("How many exercises you Worked Out Today? "),
}

pixel_response = requests.post(adding_pixel_endpoint, json=pixel_params, headers=graph_header)
print(pixel_response.text)
