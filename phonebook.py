def copy_contact(source_file, destination_file):
    contacts = read_file(source_file)

    if not contacts:
        print("Нет контактов для копирования.")
        return

    print_data()

    try:
        index_to_copy = int(input("Введите номер контакта для копирования: "))
        if 1 <= index_to_copy <= len(contacts):
            contact_to_copy = contacts[index_to_copy - 1]

            with open(destination_file, "a", encoding="utf-8") as dest_file:
                dest_file.write(f"{contact_to_copy}\n\n")

            dest_file.close()  # Закрываем файл после записи
            print(f"Контакт успешно скопирован в файл {destination_file}.")
        else:
            print("Некорректный номер контакта.")
    except ValueError:
        print("Некорректный ввод. Введите число.")


def input_surname():
    return input("Введите фамилию контакта: ").title()


def input_name():
    return input("Введите имя контакта: ").title()


def input_patronymic():
    return input("Введите отчество контакта: ").title()


def input_phone():
    return input("Введите номер телефона контакта: ")


def input_address():
    return input("Введите адрес (город) контакта: ").title()


def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f"{surname} {name} {patronymic} {phone}\n{address}"


def data_input():
    contact = create_contact()
    with open("phonebook.txt", "a", encoding="utf-8") as f:
        f.write(f"{contact}\n\n")


def print_data(file_path="phonebook.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        contacts = f.read()
        contacts_list = contacts.strip().split("\n\n")
        for contact in enumerate(contacts_list, 1):
            print(*contact)


def read_file(file_name="phonebook.txt"):
    with open(file_name, "r", encoding="utf-8") as f:
        contacts = f.read().strip().split("\n\n")
        return contacts


def search_contact():
    print(
        "Варианты поиска: \n"
        "1- По фамилии \n"
        "2- По имени \n"
        "3- По отчеству \n"
        "4- По телефону \n"
        "5- По адресу (города)"
    )
    var = input("Выберите необходимый вариант: ")
    while var not in ("1", "2", "3", "4", "5"):
        print("Некорректный ввод данных!")
        var = input("Выберите номер действия: ")
        print()
    i_var = int(var) - 1

    find = input("Введите данные для поиска: ").title()
    print()

    contacts = read_file()
    for contact_str in contacts:
        contact_list = contact_str.replace("\n", " ").split()
        if find in contact_list[i_var]:
            print(contact_str)

    print()


def interface():
    with open("phonebook.txt", "a", encoding='utf-8'):
        pass
    choice = ""
    while choice != "5":
        print()
        print(
            "Варианты действия: \n" \
            "1 - Добавление контакта \n" \
            "2 - Вывести данные на экран \n" \
            "3 - Поиск контакта \n" \
            "4 - Скопировать данные из одного файла в другой \n" \
            "5-  Выход"
        )
        print()
        choice = input("Выберите номер действия: ")
        print()
        while choice not in ("1", "2", "3", "4"):
            print("Некорректный ввод данных!")
            choice = input("Выберите номер действия: ")
        if choice == "1":
            data_input()
        elif choice == "2":
            print_data()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            source_file = input("Введите фаил из которого будет производиться копирование: ")
            destination_file = input("Введите фаил в который будет производиться копирование: ")
            copy_contact(source_file, destination_file)
        elif choice == "5":
            print("Всего доброго!")


if __name__ == '__main__':
    interface()
