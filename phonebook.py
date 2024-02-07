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


def write_file(contacts):
    with open("phonebook.txt", "w", encoding="utf-8") as f:
        for contact in contacts:
            f.write(contact + "\n\n")


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


def update_contact():
    contacts = read_file()

    if not contacts:
        print("Нет контактов для обновления.")
        return

    print_data()

    try:
        index_to_update = int(input("Введите номер контакта для изменения: "))
        if 1 <= index_to_update <= len(contacts):
            contact_to_update_index = index_to_update - 1
            contact_to_update = contacts[contact_to_update_index]

            # Разбиваем строку контакта на фамилию, имя, отчество, телефон и адрес
            parts = contact_to_update.split()

            # Проверяем, что в строке есть необходимые элементы
            if len(parts) >= 5:
                last_name, first_name, middle_name = parts[:3]
                phone_number = parts[3]
                address = " ".join(parts[4:])  # Объединяем оставшиеся элементы в строку для адреса

                # Выводим информацию о контакте
                print("Информация о контакте:")
                print(f"Фамилия: {last_name}")
                print(f"Имя: {first_name}")
                print(f"Отчество: {middle_name}")
                print(f"Телефон: {phone_number}")
                print(f"Адрес: {address}")
                print("-----------------------------")

                # Запрашиваем у пользователя, какие данные он хочет обновить
                field_to_update = input(
                    "Введите название поля для изменения (Фамилия, Имя, Отчество, Телефон, Адрес): ").lower()

                # Проверяем, что введенное поле соответствует одному из доступных полей
                if field_to_update in ["фамилия", "имя", "отчество", "телефон", "адрес"]:
                    new_value = input(f"Введите новое значение для {field_to_update}: ")

                    # Обновляем соответствующее поле в контакте
                    if field_to_update == "фамилия":
                        last_name = new_value
                    elif field_to_update == "имя":
                        first_name = new_value
                    elif field_to_update == "отчество":
                        middle_name = new_value
                    elif field_to_update == "телефон":
                        phone_number = new_value
                    elif field_to_update == "адрес":
                        address = new_value

                    # Обновляем контакт в списке
                    contacts[
                        contact_to_update_index] = f"{last_name} {first_name} {middle_name} {phone_number}\n{address}\n"

                    # Сохраняем обновленные контакты в файл
                    write_file(contacts)
                    print("Контакт успешно обновлен.")

                else:
                    print("Некорректное название поля.")
            else:
                print(f"Ошибка в формате контакта {index_to_update}. Необходимо минимум 5 элементов.")
        else:
            print("Некорректный номер контакта.")
    except ValueError:
        print("Некорректный ввод. Введите число.")


def delete_contact():
    contacts = read_file()

    if not contacts:
        print("Нет контактов для удаления.")
        return

    print_data()

    try:
        index_to_delete = int(input("Введите номер контакта для удаления: "))
        if 1 <= index_to_delete <= len(contacts):
            contact_to_delete_index = index_to_delete - 1
            contact_to_delete = contacts[contact_to_delete_index]

            print(f"Удаляемый контакт:\n{contact_to_delete}\n")

            confirmation = input("Вы уверены, что хотите удалить этот контакт? (y/n): ").lower()
            if confirmation == "y":
                # Удаляем контакт из списка
                del contacts[contact_to_delete_index]

                # Перезаписываем обновленные данные в файл
                with open("phonebook.txt", "w", encoding="utf-8") as f:
                    f.write("\n\n".join(contacts))

                print("Контакт успешно удален.")
            else:
                print("Удаление отменено.")
        else:
            print("Некорректный номер контакта.")
    except ValueError:
        print("Некорректный ввод. Введите число.")


def interface():
    with open("phonebook.txt", "a", encoding='utf-8'):
        pass
    choice = ""
    while choice != "7":
        print(
            "Варианты действия: \n" \
            "1 - Добавление контакта \n" \
            "2 - Вывести данные на экран \n" \
            "3 - Поиск контакта \n" \
            "4 - Скопировать данные из одного файла в другой \n" \
            "5 - Обновить данные контакта \n" \
            "6 - Удалить контакт \n" \
            "7 - Выход"
        )
        print()
        choice = input("Выберите номер действия: ")
        print()

        while choice not in ("1", "2", "3", "4", "5", "6"):
            print("Некорректный ввод данных!")
            choice = input("Выберите номер действия: ")

        if choice == "1":
            data_input()
        elif choice == "2":
            print_data()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            source_file = input("Введите файл, из которого будет производиться копирование: ")
            destination_file = input("Введите файл, в который будет производиться копирование: ")
            copy_contact(source_file, destination_file)
        elif choice == "5":
            update_contact()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            print("Всего доброго!")


if __name__ == '__main__':
    interface()
