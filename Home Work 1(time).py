"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах: до минуты: <s> сек;
до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""

duration = int(input("Введите время в секундах: "))
if duration < 60:
    print(str(duration) + " сек")
elif duration < 60 * 60:
    print(str(duration // 60) + " мин " + str(duration % 60) + " сек ")
elif duration < 24 * 60 * 60:
    print(str(duration // 3600) + " час " + str(duration % 3600 // 60) + " мин " + str(duration % 60) + " сек ")
else:
    print(str(duration // (24 * 3600)) + " дн " + str(duration % (24 * 3600) // 3600) + " час " +
    str(duration % (24 * 3600) % 3600 // 60) + " мин " + str(duration % 60) + " сек ")