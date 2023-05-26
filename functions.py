def show_data() -> None:
    """Выводит информацию из справочника"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        print(book.read())


def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')


def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите найти: ')
    result = search(data, contact_to_find)
    print(result)


def search(book: str, info: str) -> list[str]:
    """Находит в списке записи по определенному критерию поиска"""
    book = book.split('\n')
    return list(filter(lambda contact: info.lower() in contact.lower(), book))


def edit_data() -> None:
    """Изменяет информацию из файла"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        tel_book = book.read()
    print(tel_book)
    index_delete_data = int(input('Введите номер строки для редактирования: ')) - 1
    tel_book_lines = tel_book.split('\n')
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(' | ')
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    num = elements[0]
    if len(fio) == 0:
        fio = elements[1]
    if len(phone_num) == 0:
        phone_num = elements[2]
    edited_line = f'{num} | {fio} | {phone_num}'
    tel_book_lines[index_delete_data] = edited_line
    print(f'Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n')
    with open('book.txt', 'w', encoding='utf-8') as book:
        book.write('\n'.join(tel_book_lines))


def delete_data() -> None:
    """Удаляет информацию из файла"""
    with open('book.txt', 'r', encoding='utf-8') as book:
        tel_book = book.read()
        print(tel_book)
    index_delete_data = int(input('Введите номер строки для удаления: ')) - 1
    tel_book_lines = tel_book.split('\n')
    del_tel_book_lines = tel_book_lines[index_delete_data]
    tel_book_lines.pop(index_delete_data)
    print(f'Удалена запись: {del_tel_book_lines}\n')
    with open('book.txt', 'w', encoding='utf-8') as book:
        book.write('\n'.join(tel_book_lines))
