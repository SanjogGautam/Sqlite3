import sqlite3
from building_database_functions import inserting_data, delete_data, see_all
# inserting_data()
n=int(input("Enter the id of the data you want to delete= "))
delete_data(n)
see_all()
