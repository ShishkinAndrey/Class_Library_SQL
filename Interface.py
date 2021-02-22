from Class_Library import Library


def _input():
    list_par = ['add', 'delete', 'edit', 'search', 'review','sort']
    input_command = input('Введите команду review-add-delete-edit-search-sort \n')
    while not input_command.isalpha() or input_command not in list_par:
        input_command = input('Error! Введите одну из команд review-add-delete-edit-search-sort \n')
    return input_command.lower()


def command_add():
    new_book = list()
    name = input('Введите имя книги')
    year = int(input('Введите год выпуска книги'))
    pages = int(input('Введите кол-во страниц книги'))
    rating = float(input('Введите рейтинг книги'))
    price = float(input('Введите цену книги'))
    author = input('Введите автора книги')
    new_book.append((name, year, pages, rating, price, author))
    return new_book


def get_number():
    number_deleted_book = input('Введите номер книги')
    return number_deleted_book


def get_field():
    edit_field = input(f'Выберите параметр').lower()
    return edit_field


def new_field_value():
    new_value = input('Введите новые данные для данного параметра')
    return new_value


def choose_reverse_sort():
    choose_reverse = input(f'Выберите способ сортировки: по возрастанию или по убыванию. '
                           f'Если по возранию - введите да, если по убыванию - нет. ').lower()
    if choose_reverse == 'нет':
        choose_reverse = 'DESC'
    elif choose_reverse == 'да':
        choose_reverse = 'ASC'
    return choose_reverse


def main_func():
    lib = Library()
    while True:
        input_command = _input()
        if input_command == 'add':
            lib.insert_book(command_add())
        elif input_command == 'delete':
            lib.delete_row(get_number())
        elif input_command == 'review':
            for book in lib.review_all_table():
                print(book)
        elif input_command == 'edit':
            lib.edit_field(get_number(), get_field(), new_field_value())
        elif input_command == 'search':
            print(lib.search_book(get_field(), new_field_value()))
        elif input_command == 'sort':
            for book in lib.sort_library(get_field(), choose_reverse_sort()):
                print(book)


if __name__ == '__main__':
    main_func()
