# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# недоделано, списано из Интернета
from math import gcd

n1, d1 = map(int, input().split('/'))
n2, d2 = map(int, input().split('/'))

if d1 == d2:
    print('{}/{}'.format(n1 + n2, d1))
else:
    cd = int(d1 * d2 / gcd(d1, d2))
    rn = int(cd / d1 * n1 + cd / d2 * n2)
    g2 = gcd(rn, cd)
    n = int(rn / g2)
    d = int(cd / g2)
    print('{}/{}'.format(n, d) if n != d else n)

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import json
import os

NORMA = 8  # константа дневная норма


# функция расчёта зарплаты
def count_sal(salary, hours, norma):
    """
    Возвращает зарплату одного работника
    """
    fee_in_hour = salary / norma
    if hours == 0:  # не работал
        return 0
    elif hours <= norma:  # нет переработки
        fee = fee_in_hour * hours
    elif hours > norma:  # переработка
        fee = (fee_in_hour * norma) + ((fee_in_hour * 2) * (hours - norma))
    return fee

# считываем данные из файла, используем модный формат json
path = os.path.join('data', 'workers.json')
with open(path, 'r', encoding='utf-8') as file_workers:
    dict_workers = json.load(file_workers)  # зарплата в месяц
path = os.path.join('data', 'hours_of.json')
with open(path, 'r', encoding='utf-8') as file_hours_of:
    dict_hours_of = json.load(file_hours_of)  # число отработанных часов в день

dict_salary = dict.copy(dict_workers)  # создаём новый словарь для хранения зарплат

# выводим дневную зарплату работников на экран
for key in dict_workers:
    dict_salary.update({key: count_sal(dict_workers[key], dict_hours_of[key], NORMA)})
print(dict_salary)
# выводим дневную зарплату работников в файл
path = os.path.join('data', 'salary.json')
with open(path, 'w', encoding='utf-8') as file_salary:
    json.dump(dict_salary, file_salary, ensure_ascii=False, indent=4)

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
import os

temp = list()
path = os.path.join('data', 'fruits.txt')
with open(path, 'r', encoding='utf-8') as file_fruits:
    list_fruits = list(file_fruits.readlines())
for fruit in list_fruits:
    path = os.path.join('data', format("fruit_{0}.txt".format(fruit[0].upper())))
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file_f:
            temp = list(file_f.readlines())
    with open(path, 'a+', encoding='utf-8') as file_f:
        if fruit not in temp:
            file_f.write(fruit)
        else:
            file_f.close()  # хуже не будет
