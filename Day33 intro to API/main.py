import requests

# get is the function that goes to the website and gets the information from it
response = requests.get(url='http://api.open-notify.org/iss-now.json')
# the value stored inside the variable response is the response code
"""
    if response code is starting with 
        1xx then it means: Hold On something is happening   
        2xx then it means: Here You GO you are getting the data you want   
        3xx then it means: Go Away
        4xx then it means: You Screwed Up
        5xx then it means: Server Screwed Up        
"""
# print(response.status_code)
# if you want to raise an error that is particularly related to the status code then you have to write more than 100
# if statements instead you can use the pre-written requests function called raise_for_status.
response.raise_for_status()

# to get the data that is being generated/passed to our API request we have to store the response into a json format
data = response.json()

latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']
iss_position = (longitude, latitude)

print(iss_position)
