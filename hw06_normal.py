__author__ = 'Юзов Евгений Борисович'

# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class School:
    def __init__(self, school_name, school_address, teachers, students):
        self._school_name = school_name
        self._school_address = school_address
        self._teachers = teachers
        self._students = students

    def get_all_classes(self):
        classes = set([student.get_class_room for student in self._students])
        return classes

    def get_students(self, class_room):
        return [student.get_short_name for student in self._students if
                class_room == student.get_class_room]

    def get_teachers(self, class_room):
        return [teacher.get_short_name for teacher in self._teachers if
                class_room in teacher.get_classes]

    def get_parents(self):
        parents = set([student.get_parent for student in self._students])
        return (parents)

    def find_student(self, student_short_name):
        for pupil in self._students: # перебираем последовательно каждый экземпляр класса Student
            if pupil.get_short_name == student_short_name:
                teachers = [teachers.get_short_name for teachers in
                            self._teachers if pupil.get_class_room in
                            teachers.get_classes]
                lessons = [teachers.get_courses for teachers in
                           self._teachers if pupil.get_class_room in
                           teachers.get_classes]
                return {
                    'short_name': student_short_name,
                    'class_room': pupil.get_class_room,
                    'teachers': teachers,
                    'lessons': lessons
                }

# общую информацию выносим в класс-предок (родитель)
class People:
    def __init__(self, name, surname, birth_date):
        self._name = name
        self._surname = surname
        self._birth_date = birth_date

    @property
    def get_full_name(self):
        return f'{self._surname} {self._name} {self._birth_date}'

    @property
    def get_short_name(self):
        return f'{self._surname} {self._name[:1]}.'


class Teacher(People):
    def __init__(self, name, surname, birth_date, courses, classes):
        People.__init__(self, name, surname, birth_date)
        self._courses = courses
        self._classes = classes

    @property
    def get_courses(self):
        return self._courses

    @property
    def get_classes(self):
        return self._classes


class Student(People):
    def __init__(self, name, surname, birth_date, class_room, mother, father):
        People.__init__(self, name, surname, birth_date)
        self._class_room = class_room
        self._parents = {'мама': mother, 'папа': father}

    @property
    def get_class_room(self):
        return self._class_room

    @property
    def get_parent(self):
        return f'{self.get_short_name}: {self._parents}'


if __name__ == '__main__':
    # Создаём списки экземпляров классов, чтобы потом передать в класс School
    students = [Student('Александр', 'Иванов', '10.11.1998', '5А', 'Иванова Н.Г.', 'Иванов З.К'),
                Student('Петр', 'Сидоров', '10.01.1995', '8Б', 'Сидорова А.С.', 'Сидоров М.Е.'),
                Student('Иван', 'Петров', '12.11.1999', '4В', 'Петрова И.Р.', 'Петров С.Н.')]
    teachers = [Teacher('Аркадий', 'Альтов', '21.12.1973', 'Java', ['5А', '8Б', '4В']),
                Teacher('Филипп', 'Киркоров', '16.11.1970', 'Python', ['5А', '8Б']),
                Teacher('Дмитрий', 'Нагиев', '03.05.1982', 'C++', ['5А', '4В'])]

    school = School('№131', 'Казань', teachers, students) # создаём экземпляр класса School

    print('\nПолный список всех классов школы:')
    print(', '.join(school.get_all_classes()))

    print('\nСписок всех учеников в 8Б классе:')
    print(', '.join(school.get_students('8Б')))

    print('\nСписок всех учителей, преподающих 4В классе:')
    print(', '.join(school.get_teachers('4В')))

    print('\nСписок всех родителей учеников:')
    print(',\n'.join(school.get_parents()))

    student = school.find_student('Сидоров П.')
    print('\nСтудент: {0}\nКласс: {1}\nУчителя: {2}\nПредметы: {3}'.format(student['short_name'],
                                                                          student['class_room'],
                                                                          ', '.join(student['teachers']),
                                                                          ', '.join(student['lessons'])))