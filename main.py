import requests
import secret_files
import datetime

#You can make your own username,token,graph_id and pixela endpoint by just login on Pixela API.

USERNAME = secret_files.s_USERNAME
TOKEN = secret_files.s_TOKEN
GRAPH_ID = secret_files.s_GRAPH_ID
pixela_endpoint = secret_files.s_pixela_endpoint
NEW_TOKEN = secret_files.s_NEW_TOKEN

parameter = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=parameter)    #run only once as this will create a user
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameter = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "mins",
    "type": "float",
    "color": "sora",
}

graph_headers = {
    "X-USER-TOKEN": TOKEN
}
#response2 = requests.post(url=graph_endpoint, json=graph_parameter, headers=graph_headers)       #Create graph ad run it only once
#print(response2.text)

value_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.datetime.now()
#print(type(today))

value_graph_parameters = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("How many min's did you coded today?: "),
}

#To update the value on graph
value_graph = requests.post(url=value_graph_endpoint, json=value_graph_parameters, headers=graph_headers)
print(value_graph.text)


#Check my graph here "https://pixe.la/v1/users/abhikesarwani38/graphs/myfirstgraph1.html"
#You will also get a graph link which you can search on any browser and see your habits updates
