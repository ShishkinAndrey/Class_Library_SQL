import sqlite3

FILENAME_DATABASE = "C:\\Users\\busin\\PycharmProjects\\SQL\\sm_app.sqlite"
COMMAND_TO_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS Library (
  number INTEGER ,
  name TEXT ,
  year INTEGER,
  pages INTEGER,
  rating FLOAT,
  price FLOAT, 
  author TEXT
);
"""
COMMAND_TO_INSERT = "INSERT INTO Library VALUES (?, ?, ?, ?, ?, ?, ?)"
COMMAND_TO_READ = 'SELECT * FROM Library'

def create_connection(path=FILENAME_DATABASE):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

    return connection


def create_table(connect, query=COMMAND_TO_CREATE_TABLE):
    cursor = connect.cursor()
    try:
        cursor.execute(query)
        connect.commit()
        print('Table is created successfully')
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")


def insert_in_table(connect, values, query=COMMAND_TO_INSERT):
    cursor = connect.cursor()
    try:
        cursor.executemany(query, values)
        connect.commit()
        print('Table is created successfully')
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")


def read_table(connect, query=COMMAND_TO_READ):
    cursor = connect.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")