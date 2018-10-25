import os
import errno

__author__: str = 'Алексей Сидорюк'


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def mk_dir(dir_name):
    try:
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
    except OSError:
        print("Ошибка создания директории")


def rm_dir(dir_name):
    try:
        os.rmdir(dir_name)
    except OSError as exc:
        if exc.errno == errno.ENOTEMPTY:
            print("Директория {} не пустая".format(dir_name))


'''
for i in range(1, 10):
    mk_dir('dir_' + str(i))

for i in range(1, 10):
    rm_dir('dir_' + str(i))
'''
