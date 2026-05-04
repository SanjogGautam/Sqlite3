from tkinter import *
from building_database_functions import inserting_data, delete_data, see_all

def handle_delete():
    # 1. Get the value from the Entry box
    target_id = entry.get()
    
    # 2. Check if it's actually a number (Security/Logic check)
    if target_id.isdigit():
        delete_data(int(target_id))
        print(f"Successfully sent ID {target_id} for deletion.")
        # Optional: Clear the entry box after deleting
        entry.delete(0, END)
    else:
        print("Error: Please enter a valid numeric ID.")

window = Tk()
window.title("Sanjogs Customers Database")
window.geometry("600x500") 
window.config(background="black")

title_label = Label(window, text="Database Management System", 
                    font=("Arial", 24, "bold"), fg="white", bg="black")
title_label.pack(pady=30)

# 1. View Button
show_button = Button(window, text="View Database Data", 
                     command=see_all, font=("Arial", 14), 
                     fg="green", bg="#111", width=20)
show_button.pack(pady=10)

# 2. Insert Button
insert_button = Button(window, text="Add New Records", 
                       command=inserting_data, font=("Arial", 14), 
                       fg="cyan", bg="#111", width=20)
insert_button.pack(pady=10)

# 3. Delete Section
entry = Entry(window, font=("Arial", 14), fg="red", bg="#222", insertbackground="white")
entry.pack(pady=5)
delete_button = Button(window, text="Delete Record", 
                       command=handle_delete, font=("Arial", 14), 
                       fg="red", bg="#111", width=20)
delete_button.pack(pady=10)

window.mainloop()