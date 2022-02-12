"""
Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""


class Error:
    def __init__(self, *args):
        self.my_list = []

    @property
    def my_input(self):

        while True:
            try:
                value = int(input('Enter value and press "Enter": '))
                self.my_list.append(value)
                print(f'Current list: {self.my_list} \n ')
            except:
                print(f"Invalid value - string and boolean")
                y_or_n = input(f'Try again? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(my_try_except.my_input)
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'You got out!'
                else:
                    return f'You got out!'


my_try_except = Error(1)
print(my_try_except.my_input)