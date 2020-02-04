# -*- coding: utf-8 -*-

"""
Проверка числа на простоту.
Простое число — натуральное (целое положительное) число, имеющее ровно два различных натуральных
делителя — единицу и самого себя.
"""

number = int(input("Enter number: "))

divider = 2
status_flag = 0

while (divider * divider <= number) and (status_flag != 1):
    if number % divider == 0:
        status_flag = 1
        break
    else:
        divider += 1

if status_flag == 1:
    print("Composite number")
else:
    print("Prime number")

