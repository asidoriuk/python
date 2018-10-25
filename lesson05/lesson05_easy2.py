import os

__author__: str = 'Алексей Сидорюк'


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dirs(path):
    if os.path.isdir(path):
        for i in os.listdir(path):
            if os.path.isdir(i):
                print(i)


list_dirs(".")
