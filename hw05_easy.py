__author__ = 'Юзов Евгений Борисович'
## -*- coding: utf-8 -*-
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os

for i in range(1, 10):
    dir_path = os.path.join(os.getcwd(), format('dir_{0}'.format(str(i))))
    try:
        os.mkdir(dir_path)
    except OSError as error:
        print(error, '\n')
        print(f'Директория {dir_path} уже существует!')
print(os.listdir(os.getcwd()), '\n')
# os.system('dir')

for i in range(1, 10):
    dir_path = os.path.join(os.getcwd(), format('dir_{0}'.format(str(i))))
    try:
        os.rmdir(dir_path)
    except OSError as error:
        print(error, '\n')
        print('Ошибка удаления директории', format('dir_{0}'.format(str(i))))
print(os.listdir(os.getcwd()), '\n')
# os.system('dir')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print(list(os.path.normpath(itm) for itm in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), itm))), '\n')

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys
import shutil
# import os

# filename = os.path.realpath(__file__)
filename = os.path.normpath(sys.argv[0])
new_filename = filename + '.dupl'
if not os.path.exists(new_filename):
    try:
        shutil.copy(filename, new_filename)
    except shutil.Error:
        print(f'Ошибка копирования файла {filename}!')
else:
    print(f'Файл {filename} не скопирован, т.к. {new_filename} уже существует!')
# print(os.path.normpath(sys.argv[0]))
# print(os.path.realpath(__file__))
# os.system(f'copy {filename}, {new_filename}')