# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
class Salary:
    def __init__(self, worker, hours_of):
        self._worker = worker
        self._hours_of = hours_of

    def get_all_workers(self):
        workers = set([itm.get_worker for itm in self._worker])
        return workers


class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname


class Worker(Person):
    def __init__(self, arg_worker):
        Person.__init__(self, arg_worker[0:0], arg_worker[0:1])
        self._salary = arg_worker[0:2]
        self._job = arg_worker[0:3]
        self._norma = arg_worker[0:4]

    @property
    def get_salary(self):
        return self._salary

    @property
    def get_norma(self):
        return self._norma

    @property
    def get_worker(self):
        return f'{self._surname} {self._name} {self._job}'


class HoursOf(Person):
    def __init__(self, arg_hours_of):
        Person.__init__(self, arg_hours_of[0:0], arg_hours_of[0:1])
        self._hours_of = arg_hours_of[0:2]

    @property
    def get_hours_of(self):
        return self._hours_of


if __name__ == '__main__':
    import os

    path = os.path.join('data', 'workers')
    worker = list()
    with open(path, 'r', encoding='utf-8') as file_workers:
        for line in file_workers:
            worker.append(Worker(line.split()))
    path = os.path.join('data', 'hours_of')
    hours_of = list()
    with open(path, 'r', encoding='utf-8') as file_hours_of:
        for line in file_hours_of:
            hours_of.append(HoursOf(line.split()))
    salary = Salary(worker, hours_of)
    print(', '.join(salary.get_all_workers()))
