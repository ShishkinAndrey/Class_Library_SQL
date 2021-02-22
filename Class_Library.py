from Library import get_library_from_json
import sqlite3


class Library:
    DEFAULT_DB_NAME = "library.sqlite"

    def __init__(self):
        self.__driver = SqliteDb(self.DEFAULT_DB_NAME)

        self.command_create_table = """
        CREATE TABLE IF NOT EXISTS Library (
          number integer primary key AUTOINCREMENT ,
          name string,
          year ,
          pages ,
          rating ,
          price ,
          author string
        );"""
        self.command_insert = "INSERT INTO Library(name,year,pages,rating,price,author) VALUES (?, ?, ?, ?, ?, ?)"
        self.command_read_all_rows = f"SELECT * FROM Library"
        self.command_delete = f"DELETE from Library where number = ?"

    def create_library_table(self):
        self.__driver.execute(self.command_create_table)

    def insert_book(self, values):
        self.__driver.executemany(self.command_insert, values)

    def review_all_table(self):
        return self.__driver.fetchall(self.command_read_all_rows)

    def search_book(self, field, field_value):
        command_get_field = f"SELECT name,year,pages,rating,price,author FROM Library WHERE {field} = {field_value}"
        return self.__driver.fetchall(command_get_field)

    def delete_row(self, number):
        self.__driver.executemany(self.command_delete, str(number))

    def edit_field(self, number, field, field_value):
        command_edit_field = f"UPDATE Library set {field} = '{field_value}' where number = {number}"
        self.__driver.execute(command_edit_field)

    def sort_library_asc(self, column):
        command_sort = f'SELECT * FROM Library ORDER BY {column}'
        self.__driver.execute(command_sort)


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
            result = self.__get_cursor().execute(query)
            self.__commit_and_close()
            return result
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



if __name__ == '__main__':
    lib = Library()
    # lib.create_library_table()
    # #
    # lib_from_json = get_library_from_json()
    # ll = []
    # for i in lib_from_json:
    #     ll.append(tuple(i.values()))
    #
    # lib.insert_book(ll)

    print(lib.review_all_table())
    # lib.edit_field(4, 'name',  'Shishkevich')
    lib.sort_library('year')
    print(lib.review_all_table())
    # new_row = lib.get_field('year', 1984)
    # print(new_row)
    # lib.insert_book(new_row)
    # lib.delete_row(2)
