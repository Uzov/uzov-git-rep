# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    """
    Возвращает ряд Фибоначчи с n-элемента до m-элемента
    """
    fib = [1, 1]
    i = 1
    while i < m:
        fib.append(fib[i - 1] + fib[i])
        i += 1
    fib = fib[(n - 1):m]
    return fib


print(fibonacci(10, 20))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    j = 0
    while j < int(len(origin_list) - 1):
        i = 0
        while i < int(len(origin_list) - 1):
            if origin_list[i] > origin_list[i + 1]:
                temp = origin_list[i]
                origin_list[i] = origin_list[i + 1]
                origin_list[i + 1] = temp
            i += 1
        j += 1
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, data):
    result = func(data)
    return result

a = [1, -4, 6, 8, -10]
print('Список: ', a)
print('Минимум: ', my_filter(min, a))
print('Максимум: ', my_filter(max, a))
print('Сумма: ', my_filter(sum, a))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
def IsParallelogr (a):
    if ((abs(a[0][0] - a[1][0]) == abs(a[2][0] - a[3][0])) and (abs(a[0][1] - a[1][1]) == abs(a[2][1] - a[3][1]))) or \
        ((abs(a[0][0] - a[2][0]) == abs(a[1][0] - a[3][0])) and (abs(a[0][1] - a[2][1]) == abs(a[1][1] - a[3][1]))):
        return 'это параллелограмм'
    else:
        return 'это не параллелограмм'
b = [[1, 6], [3, 10], [11, 5], [9,1]]
c = [[11, 13], [11, 9], [16, 9], [16, 13]]
d = [[11, 15], [15, 9], [16, 10], [11, 13]]
print(IsParallelogr(b))
print(IsParallelogr(c))
print(IsParallelogr(d))