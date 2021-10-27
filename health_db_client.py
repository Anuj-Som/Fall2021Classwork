import requests


patient1 = {"name": "Ann Ables", "id": 201, "blood_type": "A+", "dob": "12/2/2000"}
patient2 = {"name": "Bob Boyles", "id": 302, "blood_type": "O-"}
patient3 = {"name": "Chris Chou", "id": "552", "blood_type": "AB-"}

test1 = {"id": 201, "test_name": "Kidney", "test_result": 204}

r = requests.post("http://127.0.0.1:5000/new_patient", json=patient1)
print(r.status_code)
print(r.text)

r = requests.post("http://127.0.0.1:5000/add_test", json=test1)
print(r.status_code)
print(r.text)