def interface():
	print("Blood Calculator")
	keep_running = True
	while keep_running:
		print("Make a choice")
		print("1 - HDL Analysis")
		print("9 - Quit")
		choice = input("Make a choice: ")
		if choice == '9':
			keep_running = False
		elif choice == '1':
			HDL_Driver()
	
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


interface()
