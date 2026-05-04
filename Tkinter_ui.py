from tkinter import *
from building_database_functions import inserting_data, delete_data, see_all

window = Tk()
window.title("MBM Customers Database")
window.geometry("600x500") 
window.config(background="black")

# Title Label
title_label = Label(window, text="Database Management System", 
                    font=("Arial", 24, "bold"), fg="white", bg="black")
title_label.pack(pady=30)

# 1. View Button
# Note: see_all needs to return data or print to console for now
show_button = Button(window, text="View Database Data", 
                     command=see_all, font=("Arial", 14), 
                     fg="green", bg="#111", width=20)
show_button.pack(pady=10)

# 2. Insert Button
insert_button = Button(window, text="Add New Records", 
                       command=inserting_data, font=("Arial", 14), 
                       fg="cyan", bg="#111", width=20)
insert_button.pack(pady=10)

# 3. Delete Button
# WARNING: This will need a way to pass the ID later!
delete_button = Button(window, text="Delete Record", 
                       command=delete_data, font=("Arial", 14), 
                       fg="red", bg="#111", width=20)
delete_button.pack(pady=10)

window.mainloop()