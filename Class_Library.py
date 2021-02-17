from SQL_script import create_connection, create_table, insert_in_table, read_table
from Library import get_library_from_json

if __name__ == '__main__':
    connection = create_connection()
    create_table(connection)
    lib = get_library_from_json()
    ll = []
    for i in lib:
        ll.append(tuple(i.values()))
    insert_in_table(connection, ll)
    result = read_table(connection)
    for i in result:
        print(i)