__author__ = 'Юзов Евгений Борисович'
## -*- coding: utf-8 -*-

import os


def my_make_dir(dir_name: str):
    """
    Создаёт папку в текущей директории
    """
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        return True
    except OSError as error:
        print(error)
        print(f'Папка {dir_name} уже существует!')
        return False


def my_del_dir(dir_name: str):
    """
    Удаляет папку из текущей директории
    """
    dir_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isdir(dir_path):
        try:
            os.rmdir(dir_path)
            return True
        except OSError as error:
            print(error)
            print(f'Ошибка удаления папки {dir_name}!')
            return False
    else:
        print(f'Ошибка удаления папки: папка {dir_name} не существует!')
        return False


def my_list_dir():
    """
    Просматривает содержимое текущей папки
    """
    return os.listdir(os.getcwd())


def my_change_dir(dir_name: str):
    """
    Переходит в заданную папку
    """
    if os.path.isdir(dir_name):
        try:
            os.chdir(dir_name)
            return True
        except OSError as error:
            print(error)
            print(f'Ошибка перехода в папку {dir_name}!')
            return False
    else:
        print(f'Ошибка перехода в папку {dir_name}, она не существует!')
        return False