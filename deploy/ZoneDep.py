import requests, json


url = "https://192.168.0.20/api/2.0/vdn/scopes?inUniveral=true"
user = "admin"
pwd =  "M1nd!iaas"
headers = {"content-type": "application/xml"}
method = "POST"

obj = "<vdnScope><name>test-nano!</name><clusters><cluster><cluster><objectId>domain-c74</objectId></cluster></cluster></clusters></vdnScope>"

req = requests.post(url, auth=(user,pwd), data=obj, headers=headers, verify=False)

print(req)