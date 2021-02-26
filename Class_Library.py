import sqlite3

from Library import get_library_from_json


class Library:
    DEFAULT_DB_NAME = "library.sqlite"

    def __init__(self):
        self.__driver = DbContextManager(sqlite3, self.DEFAULT_DB_NAME)

        self.command_create_table = """
        CREATE TABLE IF NOT EXISTS Library (
          number INTEGER PRIMARY KEY AUTOINCREMENT ,
          name TEXT,
          year INTEGER,
          pages INTEGER,
          rating REAL,
          price REAL,
          author TEXT
        );"""
        self.command_insert = "INSERT INTO Library(name,year,pages,rating,price,author) VALUES (?, ?, ?, ?, ?, ?)"
        self.command_read_all_rows = f"SELECT * FROM Library"
        self.command_delete = f"DELETE from Library where number = ?"

    def create_library_table(self):
        with self.__driver as cursor:
            cursor.execute(self.command_create_table)

    def insert_book(self, values):
        with self.__driver as cursor:
            cursor.executemany(self.command_insert, values)

    def review_all_table(self):
        with self.__driver as cursor:
            cursor.execute(self.command_read_all_rows)
            return cursor.fetchall()

    def search_book(self, field, field_value):
        command_get_field = f"SELECT name,year,pages,rating,price,author FROM Library WHERE {field} = {field_value}"
        with self.__driver as cursor:
            cursor.execute(command_get_field)
            return cursor.fetchall()

    def delete_row(self, number):
        with self.__driver as cursor:
            cursor.executemany(self.command_delete, str(number))

    def edit_field(self, number, field, field_value):
        command_edit_field = f"UPDATE Library set {field} = '{field_value}' where number = {number}"
        with self.__driver as cursor:
            cursor.execute(command_edit_field)

    def sort_library(self, column, reverse):
        command_sort = f'SELECT * FROM Library ORDER BY {column} {reverse}'
        with self.__driver as cursor:
            cursor.execute(command_sort)
            return cursor.fetchall()


class DbContextManager:
    def __init__(self, driver, database_name):
        self.__driver = driver
        self.database_name = database_name

    def __enter__(self):
        """Выполняет подключение к БД и возвращает курсор для выполнения SQL запросов."""
        print("Каждый раз при входе в контекстный менеджер создаем объект Connection и Cursor")
        self.connection = self.__driver.connect(self.database_name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
               Автоматически закрывает все соединения.
               В зависимости от успеха выполнения SQL запроса отменяет или применяет изменения.
               """
        print("Начинаем выход из контекстного менеджера ...")
        print("Закрываем курсор ...")
        self.cursor.close()
        if isinstance(exc_type, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()


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
    # print(lib.search_book('pages', 293))
    print(lib.review_all_table())
    # lib.edit_field(4, 'name',  'Shishkevich')

    # print(lib.sort_library('pages', 'DESC'))

    # new_row = lib.get_field('year', 1984)
    # print(new_row)
    # lib.insert_book(new_row)
    # lib.delete_row(2)
