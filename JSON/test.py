import json

tmp1 = open("./data.json", "r")
tmp2 = json.load(tmp1)

tmp3 = tmp2["book1"]["year"]

print(tmp3)