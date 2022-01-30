"""
Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
 классе должны быть реализованы методы перегрузки арифметических операторов:
 сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__floordiv__, __truediv__()).
 Эти методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
 умножение и округление до целого числа деления клеток, соответственно.
"""


class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, row_len):
        result = ['*' * row_len] * (self.nums // row_len)
        if self.nums % row_len:
            result.append('*' * (self.nums % row_len))
        return '\n'.join(result)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print('Sum of cell is:')
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print('Subtraction of cell is:')
        if self.nums < other.nums:
            raise ValueError('Ячеек в первой клетке меньше второй, вычитание невозможно!')
        return Cell(self.nums - other.nums)

    def __mul__(self, other):
        print('Multiply of cell is:')
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print('Floordiv of cell is:')
        return Cell(self.nums // other.nums)


cell1 = Cell(30)
cell2 = Cell(34)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 // cell2)
print(cell2.make_order(7))
