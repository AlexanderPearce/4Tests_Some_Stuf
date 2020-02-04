# -*- coding: utf-8 -*-

"""
Найти Наибольший Общий Делитель
Пример:

Найти НОД для 30 и 18.
30 / 18 = 1 (остаток 12)
18 / 12 = 1 (остаток 6)
12 / 6 = 2 (остаток 0)
Конец: НОД – это делитель 6.
НОД (30, 18) = 6
"""

number1 = 30
number2 = 18

while (number1 != 0) and (number2 != 0):
    if number1 > number2:
        number1 = number1 % number2
    else:
        number2 = number2 % number1

print(number1 + number2)
