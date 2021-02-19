from Library import get_library_from_json
import sqlite3


class Library:
    DEFAULT_DB_NAME = "library.sqlite"

    def __init__(self):
        self.__driver = SqliteDb(self.DEFAULT_DB_NAME)

        self.command_create_table = """
        CREATE TABLE IF NOT EXISTS Library (
          number integer primary key AUTOINCREMENT ,
          name ,
          year ,
          pages ,
          rating ,
          price ,
          author 
        );"""
        self.command_insert = "INSERT INTO Library(name,year,pages,rating,price,author) VALUES (?, ?, ?, ?, ?, ?)"
        self.command_read = f"SELECT * FROM Library"
        self.command_delete = f"DELETE from Library where number = ?"

    def create_library_table(self):
        self.__driver.execute(self.command_create_table)

    def insert_book(self, values):
        self.__driver.executemany(self.command_insert, values)

    def review_all_table(self):
        return self.__driver.fetchall(self.command_read)

    def get_field(self, query, field):
        ...


class SqliteDb:
    def __init__(self, database_name: str):
        self.database_name = database_name
        self.connection = self.create_connection(self.database_name)

    @staticmethod
    def create_connection(path):
        connection = None
        try:
            connection = sqlite3.connect(path)
            print("Connection to SQLite DB successful")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
        return connection

    def __get_cursor(self):
        cursor = self.connection.cursor()
        return cursor

    def __commit_and_close(self):
        self.connection.commit()
        self.__get_cursor().close()

    def execute(self, query):
        try:
            self.__get_cursor().execute(query)
            self.__commit_and_close()
            print('Query successfully')
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")

    def executemany(self, query, values=None):
        try:
            self.__get_cursor().executemany(query, values)
            self.__commit_and_close()
            print('Query successfully')
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")

    def fetchall(self, query):
        cursor = self.__get_cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            self.__commit_and_close()
            return result
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")

    #
    # def delete_row(self, id_row):
    #     connect = self.connection
    #     cursor = connect.cursor()
    #     try:
    #         cursor.execute(self.command_delete, (id_row, ))
    #         connect.commit()
    #         cursor.close()
    #         print('Row is deleted successfully')
    #     except sqlite3.Error as e:
    #         print(f"The error '{e}' occurred")

if __name__ == '__main__':
    lib = Library()
    # lib.create_library_table()

    # lib_from_json = get_library_from_json()
    # ll = []
    # for i in lib_from_json:
    #     ll.append(tuple(i.values()))

    # lib.insert_book(lib.command_insert, ll)
    # l.delete_row('3')
    print(lib.review_all_table())
