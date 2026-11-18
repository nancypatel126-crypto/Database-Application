
import sqlite3

DATABASE_NAME = "database.db"


# Connect to Database
def connect_database():
    return sqlite3.connect(DATABASE_NAME)


# Create Table
def create_table():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            city TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

    print("Database and table ready!")


# Insert Record
def insert_record(name, email, age, city):
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO records (name, email, age, city)
        VALUES (?, ?, ?, ?)
    """, (name, email, age, city))

    conn.commit()
    conn.close()

    print("Record inserted successfully!")


# View Records
def view_records():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records")
    records = cursor.fetchall()

    if records:
        print("\n===== DATABASE RECORDS =====")

        for record in records:
            print("--------------------------")
            print("ID:", record[0])
            print("Name:", record[1])
            print("Email:", record[2])
            print("Age:", record[3])
            print("City:", record[4])
    else:
        print("No records found!")

    conn.close()


# Search Record
def search_record(record_id):
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM records WHERE id = ?",
        (record_id,)
    )

    record = cursor.fetchone()

    if record:
        print("\nRecord Found:", record)
    else:
        print("Record not found!")

    conn.close()


# Update Record
def update_record(record_id, name, email, age, city):
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE records
        SET name = ?, email = ?, age = ?, city = ?
        WHERE id = ?
    """, (name, email, age, city, record_id))

    conn.commit()

    if cursor.rowcount > 0:
        print("Record updated successfully!")
    else:
        print("Record not found!")

    conn.close()


# Delete Record
def delete_record(record_id):
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM records WHERE id = ?",
        (record_id,)
    )

    conn.commit()

    if cursor.rowcount > 0:
        print("Record deleted successfully!")
    else:
        print("Record not found!")

    conn.close()
