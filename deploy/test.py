import requests

url = 'https://192.168.0.20/api/2.0/vdn/controller'
user = 'admin'
pwd =  'M1nd!iaas'
headers = {"Accept": "application/json"}


res = requests.get(url, auth=(user,pwd), headers=headers, verify=False)
print(res.json)
