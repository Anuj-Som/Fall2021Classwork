from flask import Flask, request, jsonify
import logging
from pymodm import connect, MongoModel, fields

app = Flask(__name__)
db = []


def initialize_server():
    logging.basicConfig(filename="health_db_server.log", level=logging.DEBUG)
    connect("mongodb+srv://User1:Password@cluster0.a532e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    print("connected")

    
@app.route("/", methods=["GET"])
def status():
    return "Server is on"


@app.route("/new_patient", methods=["POST"])
def new_patient():
    """Implements /new_patient route for adding a new patient to server
    database

    The /new_patient route is a POST request that should recieve a JSON-endcoder string
    with the following format:

    {"name": str, "id": int, "blood_type": str}

    Returns:
        str or int, 
    """
    in_data = request.get_json()
    error_string, status_code = validate_input(in_data, {"name": str, "id": int, "blood_type": str})
    if error_string is not True:
        return error_string, status_code
    new_patient = add_database_entry(in_data["name"], in_data["id"], in_data["blood_type"])
    return "Added patient {}".format(new_patient)


def validate_input(in_data, expected_keys):
    if type(in_data) is not dict:
        return "The input was not a dictionary.", 400
    for key in expected_keys:
        if key not in in_data:
            return "The key {} is missing from input".format(key), 400
        if type(in_data[key]) is not expected_keys[key]:
            return "The key {} has the wrong data type".format(key), 400
    return True, 200

@app.route("/add_test", methods=["POST"])
def patient_tests():
    in_data = request.get_json()
    error_string, status_code = validate_patient_tests_input(in_data)
    if error_string is not True:
        return error_string, status_code
    added_tests = add_test_entry(in_data["id"], in_data["test_name"], in_data["test_result"])
    return "Added patient test data {}".format(str(added_tests))


def validate_patient_tests_input(in_data):
    if type(in_data) is not dict:
        return "The input was not a dictionary.", 400
    expected_keys = {"id": int, "test_name": str, "test_result": int}
    for key in expected_keys:
        if key not in in_data:
            return "The key {} is missing from input".format(key), 400
        if type(in_data[key]) is not expected_keys[key]:
            return "The key {} has the wrong data type".format(key), 400
    patient = get_patient(in_data["id"])
    if patient is None:
        return "No patient with id:{} in database".format(in_data["id"]), 400
    return True, 200


class Patient(MongoModel):
    name = fields.CharField()
    id = fields.IntegerField(primary_key=True)
    blood_type = fields.CharField()
    tests = fields.ListField()


def add_database_entry(patient_name, id_no, blood_type):
    # new_patient = {"name": patient_name,
    #                 "id": id_no,
    #                 "blood_type": blood_type,
    #                 "tests": []}
    new_patient = Patient(name=patient_name,
                          id=id_no,
                          blood_type=blood_type)
    #db.append(new_patient)
    answer = new_patient.save()
    return answer


def add_test_entry(id_no, test_name, test_result):
    patient = get_patient(id_no)
    tup = (test_name, test_result)
    patient["tests"].append(tup)
    return tup


def get_patient(id_no):
    for patient in db:
        if patient["id"] == id_no:
            return patient
    return None
        

if __name__ == "__main__":
    initialize_server()
    app.run()

