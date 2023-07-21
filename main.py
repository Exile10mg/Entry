import tkinter
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    accept = accept_var.get()

    if accept == "Accepted":
        
      # User Info GET
      firstname = first_name_entry.get()
      lastname = last_name_entry.get()
      title = title_combobox.get()
      age = age_spinbox.get()
      nationality = nationality_combobox.get()

      # Course Info GET
      registration_status = reg_status_var.get()
      numcourses = numcourses_spinbox.get()
      numsemestres = numsemestrs_spinbox.get()
      # TEST PRINT
      print(f"""Imię: {firstname}
Nazwisko: {lastname}
Tytuł: {title}
Wiek: {age}
Narodowość: {nationality}""")
      print("-------------------")
    else:
        messagebox.showwarning(title="ERROR", message="You have to accept terms and conditions!")

# Engine
window = tkinter.Tk()
# Title
window.title("Entry Data - Mike 2023")

# Main frame
frame = tkinter.Frame(window)
frame.pack()

# Saving User Info FRAME
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

# First Name
first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)

# Last Name
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

# First Name Entry
first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)

# Last Name Entry
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

# Title
title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

# Age
age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

# Nationality
nationality_lavel = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Poland", "Holland", "Germany", "French", "Czech Republic"])
nationality_lavel.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

# PADY PADX for everything
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info FRAME
courses_frame = tkinter.LabelFrame(frame, text="Course Information")
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

# Registered 
registered_label = tkinter.Label(courses_frame, text="Registration Status")

reg_status_var = tkinter.StringVar(value="Not registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered", variable=reg_status_var, onvalue="Registered", offvalue="Not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

# NumCourses
numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

#NumSemestrs
numsemestrs_label = tkinter.Label(courses_frame, text="# Semesters")
numsemestrs_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numsemestrs_label.grid(row=0, column=2)
numsemestrs_spinbox.grid(row=1, column=2)

# PADY PADX for everything
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Terms Info FRAME
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

# Terms Check BUTTON
accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.", 
                                  variable=accept_var, 
                                  onvalue="Accepted",
                                  offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid(row=3, column=0, padx=20, pady=10, sticky="news")

# Engine Loop
window.mainloop()