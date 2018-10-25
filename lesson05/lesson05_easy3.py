import os
import shutil
import inspect

__author__: str = 'Алексей Сидорюк'


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def get_my_copy():
    # Если lesson05_easy3.py где-то подключен как модуль, и сделан вызов get_my_copy()
    try:
        frame = inspect.stack()[1]
        filename = frame[0].f_code.co_filename
        shutil.copyfile(filename, "copy_" + os.path.split(filename)[1])
    # Если запустили сам lesson05_easy3.py
    except IndexError:
        shutil.copyfile(os.path.split(__file__)[1], "copy_" + os.path.split(__file__)[1])


get_my_copy()
