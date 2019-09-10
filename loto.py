__author__ = 'Юзов Евгений Борисович'
## -*- coding: utf-8 -*-
# !/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""
import random
import sys
import numpy


# import time


class Cask:
    """
    Определяем бочонок как объект-итератор, т.е. будем перебирать бочонки функцией next()
    """

    def __init__(self, count, start=-1):
        self.j = start
        self.count = count
        self._cask = random.sample(range(1, self.count + 1, 1), self.count)
        # range() возвращает диапазон x, где 1<=x[i]<91. Проверил на практике

    def __next__(self):
        # Объект считается итератором - если у него есть метод __next__, но не только: у него должен быть метод __iter__
        if self.j < self.count - 1:
            self.j += 1
            return self._cask[self.j]
        else:
            raise StopIteration

    def __iter__(self):
        # Метод __iter__ должен возвращать объект-итератор. Иначе next() ругается, что вы подставили неитерируемый объект
        return self


class Lotto:
    def __init__(self, count=90, row=3, column=5):
        self._row = row
        self._column = column
        self._count = count
        self.__gen_card()

    def __gen_card(self):
        # Номера в карточке
        self._card_num = random.sample(range(1, self._count + 1, 1), self._row * self._column)
        # Позиции номеров в карточке в трёх строках
        card_column = random.sample(range(0, 9), self._column) + \
                      random.sample(range(0, 9), self._column) + \
                      random.sample(range(0, 9), self._column)
        # Генератор номеров строк
        card_row = [0 for _ in range(self._column)] + \
                   [1 for _ in range(self._column)] + \
                   [2 for _ in range(self._column)]
        # Собираем карточку в один список (строка),(столбец),(номер)
        card = list(zip(card_row, card_column, self._card_num))
        self._matrix = numpy.zeros((3, 9))
        for i in range(0, self._row * self._column):
            self._matrix[card[i][0], card[i][1]] = card[i][2]

    def print_card(self):
        print(self._matrix)
        # Можно помучиться с форматирванием, в виде матрицы тоже понятно
        print('{:-^39}'.format('-'))

    def search_num(self, num_to_search):
        pass


class Player(Lotto):
    def __init__(self, name, score=0):
        Lotto.__init__(self)
        self._name = name
        self._score = score


if __name__ == '__main__':
    KEG_COUNT = 90  # Константа количество бочонков
    keg = Cask(KEG_COUNT)
    player1 = Player('Игрок - человек:')
    player2 = Player('Игрок - компьютер:')
    print('\n', player1._name)
    player1.print_card()
    print('\n', player2._name)
    player2.print_card()
    while True:
        try:
            keg_curr = next(keg)
            print(f'Новый бочонок: {keg_curr} (осталось {str(keg.count - keg.j - 1)})')
        except StopIteration:
            print(f'Бочонки закончились, никто не победил!')
            sys.exit(1)

#        inp_user = input('Зачеркнуть цифру? (y/n)')
#       if inp_user == 'y':
#            if player1.search(game.card_user, num_cask):
#                continue
#            else:
#                print('Game Over')
#               sys.exit(1)
#        if inp_user == 'n':
#            if player1.search(game.card_user, num_cask):
#                print('Game Over')
#                sys.exit(1)
#            elif player2.search(game.card_comp, num_cask):
#                continue
#        if inp_user != 'n' and inp_user != 'y':
#            print('Введите y or n')
#            time.sleep(1)
#            continue
