import sqlite3
def inserting_data():
    with sqlite3.connect("customers.db") as conn:
        c=conn.cursor()
        n=int(input("Enter the number of data you want to inesrt?"))
        d=[]
        for i in range(n):
            a=input(f"{i+1}. Enter your name= ")
            b=input(f"{i+1}. Enter email= ")
            d.append((a,b))
        c.executemany("insert into customers(name,email) values(?,?)",d)
        print(f"\nSuccess! {n} records inserted.")
def delete_data(n):
    with sqlite3.connect("customers.db") as conn:
        c=conn.cursor()
        c.execute("delete from customers where id= ?",(n,))
        print("Data Deleted successfully!")
def see_all():
    with sqlite3.connect("customers.db") as conn:
        c=conn.cursor()
        c.execute("select * from customers")
        a=c.fetchall()
        for i in a:
            print(f"ID= {i[0]}\tName= {i[1]}\tEmail= {i[2]}")
        print("\nAll data displayed successfully!")