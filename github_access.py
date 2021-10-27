import requests

server_name = "http://vcm-21170.vm.duke.edu:5000"

r = requests.get(server_name)

d = {
   "name": "Anuj Som",
   "net_id": "as989",
   "e-mail": "as989@duke.edu"
}

r = requests.post(server_name+"/student", json=d)
print(r.json())


