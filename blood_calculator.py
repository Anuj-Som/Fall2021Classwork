def interface():
	print("Blood Calculator")
	keep_running = True
	while keep_running:
		print("Make a choice")
		print("1 - HDL Analysis")
		print("2 - LDL Analysis")
		print("9 - Quit")
		choice = input("Make a choice: ")
		if choice == '9':
			keep_running = False
		elif choice == '1':
			HDL_Driver()
		elif choice == '2':
			LDL_Driver()
	
	print(choice)
	return choice

def HDL_Driver():
	hdl_value = hdl_input()
	hdl_character = hdl_analysis(hdl_value)
	hdl_output(hdl_value, hdl_character)

def hdl_input():
	hdl_value = int(input(("Enter HDL Value: ")))
	return hdl_value

def hdl_analysis(HDL_value):
	if HDL_value >= 60:
		return "Normal"
	elif 40 <= HDL_value < 60:
		return "Borderline Low"
	else:
		return "Low"

def hdl_output(HDL_value, HDL_character):
	print("The HDL value of {} is considered {}".format(HDL_value, HDL_character))
	return

def LDL_Driver():
	ldl_value = ldl_input()
	ldl_character = ldl_analysis(ldl_value)
	ldl_output(ldl_value,ldl_character)

def ldl_input():
	ldl_value = int(input(("Enter LDL Value: ")))
	return ldl_value

def ldl_analysis(LDL_value):
	if LDL_value >= 190:
		return "very high"
	elif 160 <= LDL_value < 190:
		return "high"
	elif 130 <= LDL_value < 160:
		return "borderline high"
	else:
		return "normal"
	return

def ldl_output(LDL_value, LDL_character):
	print("The LDL value of {} is considered {}".format(LDL_value, LDL_character))
	return	


interface()
