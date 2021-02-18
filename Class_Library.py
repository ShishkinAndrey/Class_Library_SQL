from SQL_script import create_connection, create_table, insert_in_table, read_table
from Library import get_library_from_json
import sqlite3


class Library():
    def __init__(self, database_name: str):
        self.database_name = database_name
        self.connection = self.create_connection(self.database_name)
        self.command_create_table = """
        CREATE TABLE IF NOT EXISTS Library (
          number integer primary key AUTOINCREMENT ,
          name  ,
          year ,
          pages ,
          rating,
          price ,
          author
        );"""
        self.command_insert = "INSERT INTO Library(name,year,pages,rating,price,author) VALUES (?, ?, ?, ?, ?, ?)"
        self.default_preview = '*'
        self.command_read = f"SELECT {self.default_preview} FROM Library"

    @staticmethod
    def create_connection(path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
        return connection

    def create_table(self):
        connect = self.connection
        cursor = connect.cursor()
        try:
            cursor.execute(self.command_create_table)
            connect.commit()
            print('Table is created successfully')
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")

    def insert_in_table(self, values):
        connect = self.connection
        cursor = connect.cursor()
        try:
            cursor.executemany(self.command_insert, values)
            connect.commit()
            print('Table is created successfully')
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")

    def review(self):
        connect = self.connection
        cursor = connect.cursor()
        try:
            cursor.execute(self.command_read)
            result = cursor.fetchall()
            return result
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")

    def add(self, book: list):
        self.insert_in_table(book)

if __name__ == '__main__':

    # l = Library('library.sqlite')
    # l.create_table()
    # column = input('Введите параметры')
    # COMMAND_TO_READ = f"SELECT {column} FROM Library"
    # print(l.review(COMMAND_TO_READ))

    lib = get_library_from_json()
    ll = []
    for i in lib:
        ll.append(tuple(i.values()))
    print(ll)
    # l.insert_in_table(ll)

    # result = read_table(connection)
    # for i in result:
    #     print(i)
