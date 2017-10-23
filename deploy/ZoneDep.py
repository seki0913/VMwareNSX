import requests, json


url = "https://192.168.0.20/api/2.0/vdn/scopes?inUniveral=true"
user = "admin"
pwd =  "password"
headers = {"content-type": "application/json"}
method = "POST"

obj = {
    "vdnScope": [
        "name": "test-dazo!",
        "clusters": [
            "cluster": {
                "cluster": {
                    "objectId":"domain-c74"
                }
            }
        ]
    ]
}

obj_json = json.dumps(obj)

req = requests.post(url, auth=(user,pwd), data=obj_json, headers=headers, verify=False)

print(req)
