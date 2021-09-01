print("This is the database.py module")
print("It's name is {}".format(__name__))

import blood_calculator as bc
# from blood_calculator import hdl_analysis
# from blood_calculator import *

answer = bc.hdl_analysis(55)
print("The analysis of 55 HDL is {}".format(answer))

answer2 = bc.ldl_analysis(200)
print("The analysis of 200 LDL is {}".format(answer2))



