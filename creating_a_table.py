import sqlite3
conn=sqlite3.connect("customers.db")
c=conn.cursor()
#creatinga table
#sqlite3 is case insensitive
c.execute("""CREATE table if not exists customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)""")
#inserting data into the table
c.execute("insert into customers(name,email) values('Sanjog Gautam','sanjog.gautam@gmail.com')")
conn.commit()
#fetching data from the table
c.execute("select * from customers")
print(c.fetchall())