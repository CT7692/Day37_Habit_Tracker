import os
from datetime import datetime
from security import safe_requests

TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = os.environ.get("GRAPH_ID")
USERNAME = "jrydel92"


pixela_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
now = datetime.now()
today = now.strftime("%Y%m%d")
qty = str(10)

header = {
    "X-USER-TOKEN": TOKEN
}

post_parameters = {
    "date": today,
    "quantity": qty
}

response = safe_requests.post(url=pixela_endpoint, json=post_parameters, headers=header)
