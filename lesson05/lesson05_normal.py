import os
import lesson05_easy1
import lesson05_easy2

__author__: str = 'Алексей Сидорюк'


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

def print_help():
    print("help - получение справки")
    print("exit - выход")
    print("1 - перейти в папку")
    print("2 - Просмотреть содержимое текущей папки")
    print("3 - Удалить папку")
    print("4 - Создать папку")


do = {
    "help": print_help,
    "1": os.chdir,
    "2": lesson05_easy2.list_dirs,
    "3": lesson05_easy1.rm_dir,
    "4": lesson05_easy1.mk_dir
}

while True:
    act_str = input("Выберите действие (help - получение справки): ")
    if act_str != "exit":
        if act_str == "1":
            dir_name = input("Введите название директории для перехода: ")
            if dir_name:
                dir_path = os.path.join(os.getcwd(), dir_name)
                try:
                    do[act_str](dir_path)
                    print("Успешно перешли в " + dir_path)
                except FileNotFoundError:
                    print("Нет такой директории.")
            else:
                print("Остаемся в текущей директории.")
        elif act_str == "2":
            do[act_str](".")
        elif act_str == "3":
            dir_name = input("Введите название директории для удаления: ")
            if dir_name:
                do[act_str](dir_name)
        elif act_str == "4":
            dir_name = input("Введите название директории для создания: ")
            if dir_name:
                do[act_str](dir_name)
        elif act_str == "help":
            do[act_str]()
    elif act_str == "exit":
        break
