"""

# 55.  Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Поиск по фамилии
from func import *


privet()

# 1 - Интерфейс
# 2 - работа с файлом
# 3 - алгоритм


# 1 - добавление контакта
# 2 - вывод всех
# 3 - поиск по фамилии
# 4 - выход

"""
def create(path):
    try:
        file = open(path, 'r')
    except IOError:
        print('Создан новый справочник -> phone_book.txt ')
        file = open(path, 'w')
    finally:
        file.close()

def add_cont(file_name, stroka):
    data = open(file_name, 'a')
    data.write(stroka + "\n")
    data.close()

def show_all(file_name):
    data = open(file_name, "r")
    for line in data:
        print(line[:-1])
    data.close()

def search(file_name, find_contact):
    with open(file_name, "r") as f:
        for contact in f:
            if find_contact in contact:
                return "Контакт: " + contact
    return "нет такого контакта"

def del_contact(file_name, value):
    with open(file_name, "r") as f:
        contacts = f.readlines()
    with open(file_name, "w") as f:
        for contact in contacts:
            if value not in contact:
                f.write(contact)

def change_contact(file_name, old_value, new_value):
    with open(file_name, "r") as f:
        contacts = f.readlines()
    with open(file_name, "w") as f:
        for contact in contacts:
            if old_value in contact:
                f.write(new_value)
            else:
                f.write(new_value)
            