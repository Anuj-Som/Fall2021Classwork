import tkinter as tk
from tkinter import ttk
from health_db_client import add_patient_to_server


def create_output(name, id, blood_letter, rh_factor, center):
    out_string = "Patient name: {}\n".format(name)
    out_string += "Blood Type: {}{}\n".format(blood_letter, rh_factor)
    out_string += "Donation Center: {}\n".format(center)
    answer =  add_patient_to_server(name, id, "{}{}".format(blood_letter, rh_factor))
    return out_string, answer


def design_window():
    def ok_button_cmd():
        # Get needed data from GUI
        name = name_data.get()
        id = id_data.get()
        blood_letter = blood_letter_data.get()
        rh_factor = rh_data.get()
        center = donation_center_data.get()

        # Call external function, calls post request to server
        out_string, answer = create_output(name, id, blood_letter, rh_factor, center)
        
        # Update GUI
        print(out_string)
        output_string.configure(text=answer)

    def cancel_cmd():
        root.destroy()
    
    root = tk.Tk()
    root.title("Health Database GUI")
    #root.geometry("512x256")

    top_label = ttk.Label(root, text="Blood Donor Database")
    top_label.grid(column=0, row=0, columnspan=2, sticky='w')

    ttk.Label(root, text="Name").grid(column=0, row=1, sticky='e')

    name_data = tk.StringVar()
    name_entry_box = ttk.Entry(root, width=40, textvariable=name_data)
    name_entry_box.grid(column=1, row=1, sticky='w')


    ttk.Label(root, text="ID").grid(column=0, row=2, sticky='e')

    id_data = tk.StringVar()
    id_entry_box = ttk.Entry(root, width=10, textvariable=id_data)
    id_entry_box.grid(column=1, row=2, sticky='w', padx=20, pady=20)

    blood_letter_data = tk.StringVar()
    ttk.Radiobutton(root, text='A', variable=blood_letter_data, value='A').grid(column=0, row=3, sticky=tk.W)
    ttk.Radiobutton(root, text='B', variable=blood_letter_data, value='B').grid(column=0, row=4, sticky=tk.W)
    ttk.Radiobutton(root, text='AB', variable=blood_letter_data, value='AB').grid(column=0, row=5, sticky=tk.W)
    ttk.Radiobutton(root, text='O', variable=blood_letter_data, value='O').grid(column=0, row=6, sticky=tk.W)

    rh_data = tk.StringVar()
    rh_data.set("-")
    rh_checkbox = ttk.Checkbutton(root, text="Rh Positive", variable=rh_data, onvalue="+", offvalue="-")
    rh_checkbox.grid(column=1, row=4)

    ttk.Label(root, text="Nearest Donation Center").grid(column=2, row=0)

    donation_center_data = tk.StringVar()
    combo_box = ttk.Combobox(root, textvariable=donation_center_data)
    combo_box["values"] = ("Durham", "Raleigh", "Cary", "Apex")
    combo_box.state(["readonly"])
    combo_box.grid(column=2, row=1)

    output_string = ttk.Label(root)
    output_string.grid(column=0, row=10)

    ok_button = ttk.Button(root, text="Ok", command=ok_button_cmd)
    ok_button.grid(column=1, row=6)

    cancel_button = ttk.Button(root, text="Cancel", command=cancel_cmd)
    cancel_button.grid(column=2, row=6)

    root.mainloop()


if __name__ == '__main__':
    design_window()

