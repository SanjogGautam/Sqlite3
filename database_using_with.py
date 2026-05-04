import sqlite3
#with in sqlite3 is used to automatically close the connection after the block of code is executed
def init_db():
    try:
        # 1. Connect (This creates the file if it doesn't exist)
        with sqlite3.connect("customers.db") as conn:
            c = conn.cursor()

            # 2. Create table with a 'Check' for existing tables
            c.execute("""CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )""")

            # 3. Parameterized Insert (Prevents SQL Injection)
            user_data = ("Sanjog Gautam", "sanjog.gautam@gmail.com")
            c.execute("INSERT or ignore INTO customers (name, email) VALUES (?, ?)", user_data)
            
            # 4. Fetch and Display
            c.execute("SELECT  * FROM customers")
            items = c.fetchall()
            
            for item in items:
                print(f"ID: {item[0]} | Name: {item[1]} | Email: {item[2]}")

    except sqlite3.Error as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    init_db()