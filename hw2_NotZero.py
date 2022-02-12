"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""


class DivisionByZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_zero(divider, denominator):
        try:
            return divider / denominator
        except:
            return f"Can't divide by zero!"


div = DivisionByZero(10, 100)
print(DivisionByZero.divide_by_zero(10, 0))
print(DivisionByZero.divide_by_zero(110, 8.85))
print(DivisionByZero.divide_by_zero(10, 0.8))
print(div.divide_by_zero(0, 100))
