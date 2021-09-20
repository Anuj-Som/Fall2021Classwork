# print("This is the database.py module")
# print("It's name is {}".format(__name__))

# import blood_calculator as bc
# # from blood_calculator import hdl_analysis
# # from blood_calculator import *

# answer = bc.hdl_analysis(55)
# print("The analysis of 55 HDL is {}".format(answer))

# answer2 = bc.ldl_analysis(200)
# print("The analysis of 200 LDL is {}".format(answer2))

class Patient:
    def __init__(self, input_name, id_no, age):
        self.name = input_name
        self.id_no = id_no
        self.age = age
        self.test_done = []

    def __repr__(self):
        return "{} ({})".format(self.name, self.id_no)

def class_work():
    new_patient = Patient("Ann Ables", 120, 36)
    print(new_patient.id_no)
    print(new_patient.name)
    x = Patient("Bob Boyles", 24, 31)
    print(x.name)
    print(x)


def create_database_entry(patient_name, id_no, age):
    # new_patient = {"patient_name":patient_name, "id_no":id_no, "age":age, "tests":[]}
    # return new_patient
    new_patient = Patient(patient_name, id_no, age)
    return new_patient

def print_database(db):
    locations = ["Room 1", "Room 4", "ER", "Post-Op"]
    for patient, location in zip(db.values(), locations):
        print("{} - {}".format(patient.name, location))

def print_patients_over_age(age, db):
    print(patient.patient_name for patient in db if patient.age > age)

def get_patient(db, id_no):
    # return [patient for patient in db if patient["id_no"] == id_no]
    return db[id_no]

def main():
    class_work()

    db = {}
    x = create_database_entry("Ann Ables", 120, 30)
    db[x.id_no] = x
    x = create_database_entry("Bob Boyles", 24, 31)
    db[x.id_no] = x
    x = create_database_entry("Chris Chou", 33, 33)
    db[x.id_no] = x
    x = create_database_entry("David Dinkins", 14, 34)
    db[x.id_no] = x
    

    patient_id_tested = 24
    test_done = ("HDL", 65)

    patient = get_patient(db, patient_id_tested)
    patient.test_done.append(test_done)
    print(db[24].test_done)

    print_database(db)
    print(db)




if __name__ == "__main__":
    main()


