import requests
import json

url = "https://192.168.0.20/api/4.0/edges/"
user = "admin"
pwd =  "M1nd!iaas"
headers = {"Accept": "application/json"}


res = requests.post(url, auth=(user,pwd), verify=False)

print(res)