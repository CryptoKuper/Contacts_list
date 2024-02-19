def input_contact_data(prompt):
    # Функция для ввода данных контакта с преобразованием введенных данных в формат title
    return input(prompt).title()

def create_contact():
    # Функция для создания строки контакта
    surname = input_contact_data('Введите фамилию контакта: ')
    name = input_contact_data('Введите имя контакта: ')
    patronymic = input_contact_data('Введите отчество контакта: ')
    phone = input('Введите телефон контакта: ')
    address = input_contact_data('Введите адрес(город) контакта: ')
    return f'{surname} {name} {patronymic}: {phone}\n{address}\n\n'

def add_contact(file_name):
    # Функция для добавления контакта в файл
    contact_str = create_contact()
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(contact_str)

def print_contacts(file_name):
    try:
        # Попытка открыть файл для чтения
        with open(file_name, 'r', encoding='utf-8') as file:
            contacts_str = file.read()
    except FileNotFoundError:
        # Вывод сообщения, если файл не найден
        print(f'Файл {file_name} не найден.')
        return

    # Разделение строк с контактами
    contacts_list = contacts_str.rstrip().split('\n\n')
    for n, contact in enumerate(contacts_list, 1):
        print(n, contact)

def search_contact(file_name):
    # Функция для поиска контакта по различным параметрам
    search_options = ['фамилии', 'имени', 'отчеству', 'телефону', 'адресу(городу)']
    print('Возможные варианты поиска:')
    for i, option in enumerate(search_options, 1):
        print(f'{i}. По {option}')

    var = input('Выберите вариант поиска: ')
    while var not in map(str, range(1, len(search_options) + 1)):
        print('Некорректный ввод!')
        var = input('Выберите вариант поиска: ')

    i_var = int(var) - 1
    search = input(f'Введите данные для поиска {search_options[i_var]}: ').title()

    with open(file_name, 'r', encoding='utf-8') as file:
        contacts_str = file.read()

    contacts_list = contacts_str.rstrip().split('\n\n')

    found_contacts = [contact for contact in contacts_list if search in contact.split(':')[i_var]]
    
    if found_contacts:
        for found_contact in found_contacts:
            print(found_contact)
    else:
        print(f'Контакты по запросу "{search}" не найдены.')

def copy_contact(source_file, target_file):
    try:
        # Попытка открыть файл с контактами для чтения
        with open(source_file, 'r', encoding='utf-8') as source_file:
            contacts_str = source_file.read()
    except FileNotFoundError:
        # Вывод сообщения, если файл не найден
        print(f'Файл {source_file} не найден.')
        return

    # Разделение строк с контактами
    contacts_list = contacts_str.rstrip().split('\n\n')
    print('Доступные контакты для копирования:')
    for n, contact in enumerate(contacts_list, 1):
        print(n, contact)

    try:
        # Ввод номера контакта для копирования
        contact_number = int(input('Введите номер контакта для копирования: '))
        if 1 <= contact_number <= len(contacts_list):
            # Выбор контакта и добавление его в целевой файл
            selected_contact = contacts_list[contact_number - 1]
            with open(target_file, 'a', encoding='utf-8') as target_file:
                target_file.write(selected_contact + '\n\n')
            print(f'Контакт скопирован в файл {target_file}.')
        else:
            # Вывод сообщения об ошибке при некорректном номере контакта
            print('Некорректный номер контакта.')
    except ValueError:
        # Вывод сообщения об ошибке при некорректном вводе
        print('Введите корректный номер контакта.')

def interface(file_name):
    try:
        # Попытка открыть файл для записи
        with open(file_name, 'a', encoding='utf-8'):
            pass

        var = 0
        while var != '6':
            print(
                'Возможные варианты:\n'
                '1. Добавить контакт\n'
                '2. Вывести на экран\n'
                '3. Поиск контакта\n'
                '4. Копировать контакт из одного файла в другой\n'
                '5. Выход'
            )
            print()
            var = input('Выберите вариант действия: ')
            while var not in map(str, range(1, 7)):
                # Вывод сообщения об ошибке при некорректном вводе
                print('Некорректный ввод!')
                var = input('Выберите вариант действия: ')
            print()

            if var == '1':
                add_contact(file_name)
            elif var == '2':
                print_contacts(file_name)
            elif var == '3':
                search_contact(file_name)
            elif var == '4':
                # Запрос имени целевого файла и копирование контакта
                target_filename = input('Введите имя файла, в который нужно скопировать контакт: ')
                copy_contact(file_name, target_filename)
            elif var == '5':
                print('До свидания\n')

    except FileNotFoundError:
        # Вывод сообщения, если файл не найден
        print(f'Файл {file_name} не найден.')

if __name__ == '__main__':
    # Вызов основной функции интерфейса с указанием имени файла
    interface("phonebook.txt")
