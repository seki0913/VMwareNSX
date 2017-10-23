import requests
import json

url = "https://192.168.0.20/api/2.0/vdn/scopes"
user = "admin"
pwd =  "password"
headers = {"Accept": "application/json"}


res = requests.get(url, auth=(user,pwd), headers=headers, verify=False).json()
open_file = open("./output_scopes.json", "w")
json.dump(res, open_file)

print(res)
