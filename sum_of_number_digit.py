# -*- coding: utf-8 -*-

"""
Сумма разрядов числа
"""

number = input("Enter number: ")

sum_of_number_digit = 0
for num in number:
    sum_of_number_digit += int(num)

print(sum_of_number_digit)
