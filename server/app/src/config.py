import requests
import json

AUTH_HEADER = {"Authorization": "Bearer jekxp6zm4xol71zqo1d34dqzmps39jtq", "Content-Type": "application/json"}
ENDPOINT = "https://data.howl77.hasura-app.io/v1/query"
BASE_INSERT = {
    "type": "insert",
    "args": {
        "table": None,
        "objects": None
    }
}

BASE_SELECT = {
    "type": "select",
    "args": {
        "table": None,
        "columns": None
    }
}

def insert(table_name, objects, base):
    base["args"]["table"] = table_name
    base["args"]["objects"] = objects
    print base
    r = requests.post(url=ENDPOINT, data=json.dumps(base), headers=AUTH_HEADER)
    return r.text



print(insert(table_name="jobs_update", objects=[{"salary": "2400",
                                           "title": "plumbj4der",
                                           "summary": "shid4kjdt",
                                           "experience": "4d4dj",
                                           "city": "miamd4ddi"}], base=BASE_INSERT))







