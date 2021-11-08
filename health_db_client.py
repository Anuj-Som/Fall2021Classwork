import requests


# patient2 = {"name": "Bob Boyles", "id": 302, "blood_type": "O-"}
# patient3 = {"name": "Chris Chou", "id": 552, "blood_type": "AB-"}

# test1 = {"id": 201, "test_name": "Kidney", "test_result": 204}
def add_patient_to_server(name_input, id_input, blood_type_input):
    patient1 = {"name": name_input, "id": int(id_input), "blood_type": blood_type_input}
    r = requests.post("http://127.0.0.1:5000/new_patient", json=patient1)
    print(r.status_code)
    print(r.text)
    return r.text

# r = requests.post("http://127.0.0.1:5000/new_patient", json=patient2)
# print(r.status_code)
# print(r.text)

# r = requests.post("http://127.0.0.1:5000/new_patient", json=patient3)
# print(r.status_code)
# print(r.text)

# # r = requests.post("http://127.0.0.1:5000/add_test", json=test1)
# # print(r.status_code)
# # print(r.text)