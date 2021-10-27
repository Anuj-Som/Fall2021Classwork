import requests

server_name = "http://vcm-7631.vm.duke.edu:5002"

path = "/get_patients/as989"

r = requests.get(server_name + path)
d = r.json()
print(d)
print(type(d))
ids = d.values()

bt = []
for id in ids:
    blood_type = requests.get(server_name + "/get_blood_type/" + id).text
    print(blood_type)
    # print(type(blood_type))
    bt.append(blood_type)

print(bt)
if bt[0] == bt[1]:
    resp = {"Name": "as989", "Match": "Yes"}
else:
    resp = {"Name": "as989", "Match": "No"}

r = requests.post(server_name + "/match_check", json=resp)
print(r.text)
