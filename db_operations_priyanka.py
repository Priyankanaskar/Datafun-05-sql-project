import sqlite3
import pandas as pd
import pathlib
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")  # add this at the beginning of the main method

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
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

# Connect to the SQLite database (create it if it doesn't exist)
conn = sqlite3.connect("project.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Drop tables in reverse order of creation
cursor.execute('DROP TABLE IF EXISTS transactions;')
cursor.execute('DROP TABLE IF EXISTS orders;')

# Create the orders table
create_orders_table_query = '''
CREATE TABLE orders (
    Order_Id TEXT PRIMARY KEY,
    Order_Date DATE,
    Product_Id TEXT,
    Customer_Id TEXT,
    Transaction_Id TEXT,
    Order_Description TEXT
);
'''

# Execute the CREATE TABLE command
cursor.execute(create_orders_table_query)

# Create the transactions table
create_transactions_table_query = '''
CREATE TABLE transactions (
    Transaction_Id TEXT PRIMARY KEY,
    Payement_Status TEXT,
    Currency TEXT,
    Payement_Amount INTEGER,
    Payement_Method TEXT
);
'''

# Execute the CREATE TABLE command
cursor.execute(create_transactions_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

logging.info("Program ended")

# insert data from csv

def insert_data_from_csv():
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        orders_data_path = pathlib.Path("data", "orders.csv")
        transactions_data_path = pathlib.Path("data", "transactions.csv")
        orders_df = pd.read_csv(orders_data_path)
        transactions_df = pd.read_csv(transactions_data_path)
        with sqlite3.connect(db_file) as conn:
            # use the pandas DataFrame to_sql() method to insert data
            # pass in the table name and the connection
            orders_df.to_sql("orders", conn, if_exists="replace", index=False)
            transactions_df.to_sql("transactions", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")

    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()

logging.info("Program ended")  # add this at the end of the main method

