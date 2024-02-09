import sqlite3
import pandas as pd
import pathlib

# Define the database file in the current root project directory
db_file = pathlib.Path("project.db")

def create_database():
    """Function to create a database. Connecting for the first time
    will create a new database file if it doesn't exist yet.
    Close the connection after creating the database
    to avoid locking the file."""
    try:
        conn = sqlite3.connect(db_file)
        conn.close()
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating the database:", e)

def create_tables():
    """Function to read and execute SQL statements to create tables"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "create_tables.sql")
            with open(sql_file, "r", encoding="utf-8") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

def insert_records():
    """Function to read and execute SQL statements to insert records"""
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("sql", "insert_records.sql")
            with open(sql_file, "r", encoding="utf-8") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Records inserted successfully.")
    except sqlite3.Error as e:
        print("Error inserting records:", e)

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        deliveries_data_path = pathlib.Path("data", "deliveries.csv")
        matches_data_path = pathlib.Path("data", "matches.csv")
        deliveries_df = pd.read_csv(deliveries_data_path, encoding="utf-8")
        matches_df = pd.read_csv(matches_data_path, encoding="utf-8")
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            deliveries_df.to_sql("deliveries", conn, if_exists="replace", index=False)
            matches_df.to_sql("matches", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

def main():
    create_database()
    create_tables()
    insert_records()
    insert_data_from_csv()

if __name__ == "__main__":
    main()
