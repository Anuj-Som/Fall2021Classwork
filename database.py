#print("This is the database.py module")
#print("It's name is {}".format(__name__))

#import blood_calculator as bc
# from blood_calculator import hdl_analysis
# from blood_calculator import *

#answer = bc.hdl_analysis(55)
#print("The analysis of 55 HDL is {}".format(answer))

#answer2 = bc.ldl_analysis(200)
#print("The analysis of 200 LDL is {}".format(answer2))


def create_database_entry(patient_name, id_no, age):
    new_patient = [patient_name, id_no, age, []]
    return new_patient

def print_database(db):
    #for i in range(len(db)):
    #    print("{} - {}".format(i, db[i]))

    location = ["Room 1", "Room 4", "ER", "Post-OP"]
    #for i, patient in enumerate(db):
    #    print("{} - {} - {}".format(i, patient[0], location[i]))

    for patient, loc in zip(db, location):
        print("{} - {}".format(patient, loc))


def printOldPeople(age, db):
    for patient in db:
        if patient[2] > age:
            print(patient[0])

def get_patient(db, id_no):
    for patient in db:
        if patient[1] == id_no:
            return patient






def main():
    db = []
    x = create_database_entry("Ann Ables", 1, 30)
    db.append(x)
    x = create_database_entry("Bob Boyles", 2, 40)
    db.append(x)
    x = create_database_entry("Chris Chou", 3, 35)
    db.append(x)
    x = create_database_entry("David Dinkins", 4, 34)
    db.append(x)    

    patient_id_tested = 2
    test_done = ("HDL", 65)

    patient = get_patient(db, patient_id_tested)
    patient[3].append(test_done)
    patient[3].append(test_done)
    print_database(db)

if __name__ == "__main__":
    main()



