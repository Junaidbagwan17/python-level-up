import requests
from datetime import datetime

# ---------------------------------------------------------------------------------
# STEP 1.1 EXTRACT USERNAME AND TOKEN.
USERNAME = "junaidbagwan"
TOKEN = "tadave-tadave"
GRAPH_ID = "graph1"

# ---------------------------------------------------------------------------------
# STEP 1. CREATE PIXELA ACCOUNT AS SHOWn BELOW and after Running Once do comment
pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    "token":"tadave-tadave",
    "username":"junaidbagwan",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ---------------------------------------------------------------------------------
# STEP 2. Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Msc Exam Preparation",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN":TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ---------------------------------------------------------------------------------
# STEP 3. GET THE GRAPH
# SEE YOUR GRAPH BY CHANGING URL TO UR USERNAME and graphname,
# https://pixe.la/v1/users/junaidbagwan/graphs/graph1.html


# ---------------------------------------------------------------------------------
# STEP 4. Post value to the graph
pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixela_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("how many hours did you study today? HOURS="),
}
# print(pixela_data["date"])

response = requests.post(url=pixela_creation_endpoint, json=pixela_data, headers=headers)
print(response.text)

# ---------------------------------------------------------------------------------
# STEP 5. Browse again! # https://pixe.la/v1/users/a-know/graphs/test-graph.html
# https://pixe.la/v1/users/junaidbagwan/graphs/graph1.html

# ------------------------- UPDATE data ----------------------------------------
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_data = {
    "quantity":"4"
}
# response = requests.put(url=update_endpoint, json=new_data, headers=headers)
# print(response.text)

# -------------------- DELETE data ---------------------------------------------
delete_endpoint =  f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
