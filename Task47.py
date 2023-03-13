import csv


def add_entry(entries):
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    entries.append([name, surname, patronymic, phone_number])
    print("Запись успешно добавлена!")

def find_entry(entries):
    search_term = input("Введите фамилию, имя или отчество для поиска: ")
    matching_entries = []
    for entry in entries:
        if search_term.lower() in [item.lower() for item in entry]:
            matching_entries.append(entry)
    if len(matching_entries) == 0:
        print("Ничего не найдено.")
    else:
        print("Найдены следующие записи:")
        for entry in matching_entries:
            print(f"{entry[1]} {entry[0]} {entry[2]}: {entry[3]}")

def delete_entry(entries):
    search_term = input("Введите фамилию, имя или отчество записи, которую нужно удалить: ")
    matching_entries = []
    for entry in entries:
        if search_term.lower() in [item.lower() for item in entry]:
            matching_entries.append(entry)
    if len(matching_entries) == 0:
        print("Ничего не найдено.")
    elif len(matching_entries) == 1:
        entries.remove(matching_entries[0])
        print("Запись успешно удалена.")
    else:
        print("Найдены следующие записи:")
        for i, entry in enumerate(matching_entries):
            print(f"{i+1}. {entry[1]} {entry[0]} {entry[2]}: {entry[3]}")
        index_to_delete = int(input("Введите номер записи, которую нужно удалить: ")) - 1
        entries.remove(matching_entries[index_to_delete])
        print("Запись успешно удалена.")

def export_entries_to_file(entries):
    with open("contacts.txt", "w", newline="") as file:
        writer = csv.writer(file, delimiter="\t")
        writer.writerows(entries)
    print("Записи успешно экспортированы в файл.")

def import_entries_from_file(entries):
    with open("contacts.txt", "r", newline="") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            entries.append(row)
    print("Записи успешно импортированы из файла.")

def edit_entry(entries):
    search_term = input("Введите фамилию, имя или отчество записи, которую нужно изменить: ")
    matching_entries = []
    for entry in entries:
        if search_term.lower() in [item.lower() for item in entry]:
            matching_entries.append(entry)
    if len(matching_entries) == 0:
        print("Ничего не найдено.")
    elif len(matching_entries) == 1:

        new_name = input(f"Введите новое имя ({matching_entries[0][0]}): ")
        new_surname = input(f"Введите новую фамилию ({matching_entries[0][1]}): ")
        new_patronymic = input(f"Введите новое отчество ({matching_entries[0][2]}): ")
        new_phone_number = input(f"Введите новый номер телефона ({matching_entries[0][3]}): ")

        matching_entries[0][0] = new_name if new_name else matching_entries[0][0]
        matching_entries[0][1] = new_surname if new_surname else matching_entries[0][1]
        matching_entries[0][2] = new_patronymic if new_patronymic else matching_entries[0][2]
        matching_entries[0][3] = new_phone_number if new_phone_number else matching_entries[0][3]
        print("Запись успешно изменена.")
    else:
        print("Найдены следующие записи:")
        for i, entry in enumerate(matching_entries):
            print(f"{i+1}. {entry[1]} {entry[0]} {entry[2]}: {entry[3]}")
        index_to_edit = int(input("Введите номер записи, которую нужно изменить: ")) - 1

        new_name = input(f"Введите новое имя ({matching_entries[index_to_edit][0]}): ")
        new_surname = input(f"Введите новую фамилию ({matching_entries[index_to_edit][1]}): ")
        new_patronymic = input(f"Введите новое отчество ({matching_entries[index_to_edit][2]}): ")
        new_phone_number = input(f"Введите новый номер телефона ({matching_entries[index_to_edit][3]}): ")

        matching_entries[index_to_edit][0] = new_name if new_name else matching_entries[index_to_edit][0]
        matching_entries[index_to_edit][1] = new_surname if new_surname else matching_entries[index_to_edit][1]
        matching_entries[index_to_edit][2] = new_patronymic if new_patronymic else matching_entries[index_to_edit][2]
        matching_entries[index_to_edit][3] = new_phone_number if new_phone_number else matching_entries[index_to_edit][3]
        print("Запись успешно изменена.")


entries = []

while True:
    print("Выберите действие:")
    print("1. Вывести все записи")
    print("2. Добавить новую запись")
    print("3. Найти запись")
    print("4. Удалить запись")
    print("5. Экспортировать записи в файл")
    print("6. Импортировать записи из файла")
    print("7. Изменение записи")
    print("8. Выйти из программы")
    choice = input()

    if choice == "1":
        if len(entries) == 0:
            print("Нет записей")
        else:
            print("Текущие записи:")
            for entry in entries:
                print(f"{entry[1]} {entry[0]} {entry[2]}: {entry[3]}")
    elif choice == "2":
        add_entry(entries)
    elif choice == "3":
        find_entry(entries)
    elif choice == "4":
        delete_entry(entries)
    elif choice == "5":
        export_entries_to_file(entries)
    elif choice == "6":
        import_entries_from_file(entries)
    elif choice == "7":
        edit_entry(entries)
    elif choice == "8":
        print("До свидания!")
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")
