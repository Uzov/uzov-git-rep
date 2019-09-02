# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil

print('sys.argv = ', sys.argv)

def print_help():
    print("help - получение справки")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def my_cp():
    if not name:
        print("Необходимо указать имя файла вторым параметром!")
        return False
    filename = os.path.join(os.getcwd(), name)
    if not os.path.isfile(filename):
        print(f'Второй параметр {name} не является файлом в текущей папке!')
        return False
    new_filename = filename + '.dupl'
    if not os.path.exists(new_filename):
        try:
            shutil.copy(filename, new_filename)
            print(f'Файл {name} скопирован.')
            return True
        except shutil.Error:
            print(f'Ошибка копирования файла {name}!')
            return False
    else:
        print(f'Файл {name} не скопирован, т.к. его дубликат уже существует!')
        return False


def my_rm():
    if not name:
        print("Необходимо указать имя файла вторым параметром!")
        return
    filename = os.path.join(os.getcwd(), name)
    if not os.path.isfile(filename):
        print(f'Второй параметр {name} не является файлом в текущей папке!')
        return
    if os.path.exists(filename):
        try:
            os.remove(filename)
            print(f'Файл {name} удалён.')
        except OSError as error:
            print(error)
            print(f'Ошибка удаления файла {name}!')
    else:
        print(f'Файл {name} не удалён!')


def my_cd():
    if os.path.isdir(name):
        try:
            os.system(f'cd {name}')
            print(f'Текущая папка: {os.getcwd()}')
            return True
        except OSError as error:
            print(error)
            print(f'Ошибка перехода в папку {name}!')
            return False
    else:
        print(f'Ошибка перехода в папку {name}, она не существует!')
        return False

def my_ls():
    print(list(os.path.normpath(itm) for itm in os.listdir(os.getcwd())), '\n')

do = {"help": print_help,
      "cp": my_cp,
      "rm": my_rm,
      "cd": my_cd,
      "ls": my_ls
      }

try:
    name = sys.argv[2]
except IndexError:
    name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
