#pixela api :- https://docs.pixe.la/
#pixela website :- https://pixe.la/

import requests
import datetime
import secret_files

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

#response = requests.post(url=pixela_endpoint, json=parameter)
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
#response2 = requests.post(url=graph_endpoint, json=graph_parameter, headers=graph_headers)
#print(response2.text)

value_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.datetime.now()

value_graph_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many min's did you coded today?: "),
}

value_graph = requests.post(url=value_graph_endpoint, json=value_graph_parameters, headers=graph_headers)
print(value_graph.text)

'''
update_endpoint = f"{value_graph_endpoint}/{today.strftime('%Y%m%d')}"
updated_parameter = {
    "quantity": "40",
}

#updated_response = requests.put(url=update_endpoint, json=updated_parameter, headers=graph_headers)
#print(updated_response.text)

delete_endpoint = f"{value_graph_endpoint}/{today.strftime('%Y%m%d')}"
delete_response = requests.delete(url=delete_endpoint, headers=graph_headers)
print(delete_response.text)
'''

#Check your graph here "https://pixe.la/v1/users/abhikesarwani38/graphs/myfirstgraph1.html"