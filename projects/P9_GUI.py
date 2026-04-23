import tkinter as tk
from Measurement import Measurement


# measurement object
currentmeasurement = Measurement()

root = tk.Tk()
root.title("P9 GUI")
root.geometry("900x300")


def calculate_room():
    room_name =room_name_entry.get()
    feet = room_feet_entry.get()
    inches = room_inches_entry.get()

    if feet == "" or inches == "":
        result_label.config(text="Enter feet and inches")
        return
    
    feet = int(feet)
    inches = int(inches)    

    currentmeasurement.set_label(room_name)
    currentmeasurement.set_feet(feet)
    currentmeasurement.set_inches(inches)


    result_label.config(text=str(currentmeasurement))

def get_measurement_string():
    result_label.config(text=currentmeasurement.getMeasurementString())

def full_measurement():
    result_label.config(text=str(currentmeasurement))

def add_inches():
    currentmeasurement.addInches(1)
    result_label.config(text=str(currentmeasurement))

def total_inches():
    result_label.config(text=str(currentmeasurement.getTotalInches()))

def get_centimeters():
    result_label.config(text=str(currentmeasurement.getCentimeters()))

def getMetricString():
    result_label.config(text=str(currentmeasurement.getMetricString()))


# LABEL

room_label = tk.Label(root, text="Room Name:")
room_label.grid(row=0, column=0, padx=10, pady=10)

room_feet = tk.Label(root, text="Feet:")
room_feet.grid(row=0, column=2, padx=10, pady=10)

room_inches = tk.Label(root, text="Inches:")
room_inches.grid(row=0, column=4, padx=10, pady=10)

# entry boxes 

room_name_entry = tk.Entry(root)
room_name_entry.grid(row=0, column=1, padx=10, pady=10)

room_feet_entry = tk.Entry(root)
room_feet_entry.grid(row=0, column=3, padx=10, pady=10)

room_inches_entry = tk.Entry(root)
room_inches_entry.grid(row=0, column=5, padx=10, pady=10)

# button

calculate_button = tk.Button(root, text="Update Measurement", command=calculate_room)
calculate_button.grid(row=1, column=3, columnspan=10, pady=10)



measurement_string_button = tk.Button(root, text="Show Measurement String", command= get_measurement_string)
measurement_string_button.grid(row=1, column=1, padx=10, pady=10)

full_measurement_button = tk.Button(root, text= "Show Full Measurement", command= full_measurement)
full_measurement_button.grid(row=1, column=2, padx=10, pady=10)
                             

add_inches_button = tk.Button(root, text="Add Inches", command= add_inches)
add_inches_button.grid(row=1, column=3, padx=10, pady=10)


total_inches_button = tk.Button(root, text="Show Total Inches", command= total_inches)
total_inches_button.grid(row=2, column=1, padx=10, pady=10)


centimeters_button = tk.Button(root, text="Show Centimeters", command= get_centimeters)
centimeters_button.grid(row=2, column=2, padx=10, pady=10)

metric_string_button = tk.Button(root, text="Show Metric String", command= getMetricString)
metric_string_button.grid(row=2, column=3, padx=10, pady=10)


# result label

result_label = tk.Label(root, text="Calculate Room", width=40, height=3)
result_label.grid(row=3, column=0, columnspan=9, pady=20)



root.mainloop()