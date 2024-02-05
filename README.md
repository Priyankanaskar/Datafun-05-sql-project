# Datafun-05-sql-project
# 2. Project Start
"""
Project Name: Database Operations with Python and SQLite

Brief Introduction:
This project demonstrates the integration of Python with SQLite for database operations, including schema design,
SQL operations, and Python-SQL integration.

Author: Priyanka Naskar
"""

# 3. Import Dependencies
import logging
import sqlite3
from pathlib import Path

# 4. Logging Configuration
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")


schema_sql = '''
    CREATE TABLE IF NOT EXISTS authors (
        author_id TEXT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        year_born INTEGER
    );

    CREATE TABLE IF NOT EXISTS books (
        book_id TEXT PRIMARY KEY,
        title TEXT,
        year_published INTEGER,
        author_id TEXT,
        FOREIGN KEY (author_id) REFERENCES authors(author_id)
    );
'''

# Save schema_sql to a file (create_tables.sql)

with open('create_tables.sql', 'w') as create_tables_file: create_tables_file.write(schema_sql)


# SQL statements for data insertion (insert_records.sql)

insert_records_sql = '''

INSERT OR IGNORE INTO authors (author_id, first_name, last_name, year_born) VALUES
('1', 'John', 'Doe', 1980),
('2', 'Priyanka', 'Mokre', 1987),
('3', 'shay', 'Lkh', 1786),
('4', 'Yaak', 'Bak', 1877),
('5', 'Tilte', 'Sam', 1655),
('6', 'Riye', 'Ulo', 1905);
'''

#Example SQL statements for data insertion (insert_records.sql)
insert_records_books_sql = '''
INSERT INTO books (book_id, title, year_published, author_id) VALUES
('101', 'The Art of Programming', 2010, '1'),
('102', 'Data Science Basics', 2015, '2'),
('103', 'History of Computers', 2005, '3'),
('104', 'Machine Learning Fundamentals', 2018, '4'),
('105', 'Programming Languages Through Ages', 2000, '5'),
('106', 'Advanced Algorithms', 2022, '6');
'''

# Save insert_records_sql to a file (insert_records.sql)
with open('insert_records.sql', 'w') as insert_records_file:
    insert_records_file.write(insert_records_sql)

# 7. Python and SQL Integration
def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

# ... (previous code)

# 8. Define Main Function
def main():
    db_filepath = 'Sql_database.db'
    # Execute SQL operations
    execute_sql_from_file(db_filepath, 'create_tables.sql')
    execute_sql_from_file(db_filepath, 'insert_records.sql')
    # (Execute other SQL operations)

    logging.info("All SQL operations completed successfully")

# 9. Conditional Script Execution
if __name__ == "__main__":
    logging.info("Program started")
    main()
    logging.info("Program ended")