# -*- coding: utf-8 -*-

"""
Удалить дубликаты из списка
"""

lst_value = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
print("Original list: ", lst_value)

no_dup_lst = set(lst_value)
print("No duplicate list: ", sorted(list(no_dup_lst)))
