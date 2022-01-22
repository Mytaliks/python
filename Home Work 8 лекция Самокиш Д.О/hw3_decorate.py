"""
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...
@type_logger
def calc_cube(x):
   return x ** 3
a = calc_cube(5)
5: <class 'int'>
Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести
тип значения функции? Сможете ли решить задачу для именованных аргументов?
Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""


def type_logger(func):
    def wrapper(*args):
        calc = func(*args)
        if len(args) == 1:
            print(f'{args[0]}: {type(args[0])}')
        else:
            for el in args:
                print(f'{el}: {type(el)}')
        return calc

    return wrapper

@type_logger
def calc_cube(n, *args):
    return n ** 3

z = calc_cube(3, 3, 5)
print(z)