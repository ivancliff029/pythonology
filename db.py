import sqlite3

conn = sqlite3.connect('payroll.db')
print("db created")

def initializeDatabase():
    conn = sqlite3.connect('payroll.db')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS EMPLOYEES (
        ID INTEGER PRIMARY KEY NOT NULL, 
        FULLNAME TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        PHONE REAL NOT NULL,
        SALARY REAL NOT NULL,
        CATEGORY TEXT NOT NULL
    );
    ''')
    print('table created')
    conn.close()

def saveUserInfo(fullname, email, phone, salary, category):
    conn = sqlite3.connect('payroll.db')
    conn.execute('''
    INSERT INTO EMPLOYEES(FULLNAME, EMAIL, PHONE, SALARY, CATEGORY)
    VALUES (?, ?, ?, ?, ?)
    ''', (fullname, email, phone, salary, category))
    conn.commit()
    print("Data inserted successfully")
    conn.close()

def displayData():
    conn = sqlite3.connect('payroll.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.execute("SELECT * FROM EMPLOYEES")
    data = []
    for row in cursor:
        data.append(f'Fullname: {row["FULLNAME"]} Email: {row["EMAIL"]} Phone: {row["PHONE"]} Salary: {row["SALARY"]} Category: {row["CATEGORY"]}')
    conn.close()
    return "\n".join(data)

if __name__ == "__main__":
    initializeDatabase()
