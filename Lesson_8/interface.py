from functions import *

def interface(path):
    create(path)
    print(" 1 - добавление контакта \n 2 - вывод всех \n 3 - поиск по фамилии \n 4 - удаление по фамилии \n 5 - изменение по фамилии \n 6 - выход")
    enter = 0
    while enter != 6:
        enter = int(input("Введите желаемый вариант: "))
        if enter == 1: 
            add_cont(path, str(input("Введите фамилию и номер телефона через пробел: ")))
        elif enter == 2:
            print(show_all(path))
        elif enter == 3:
            search(path, str(input("Введите фамилию: ")))
        elif enter == 4:
            del_contact(path, str(input("Введите фамилию: ")))
        elif enter == 5:
            old_contact = str(input("Введите фамилию: "))
            search_result = search(path, old_contact)
            if search_result == "нет такого контакта":
                print(search_result)
                continue
            change_contact(path, old_contact, str(input("Введите ФИО и номер телефона через пробел: ")))
    print("спасибо за работу")