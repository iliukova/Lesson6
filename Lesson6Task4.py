# Task 4
# Виведіть на екран 10 рядків із значенням числа Pi.
# У першому рядку має бути 2 знаки після коми, у другому 3 і так далі.

import math
pi = math.pi
n = 2
for i in range(10):
    res = f'Pi = {pi:1.{n}f}'
    n += 1
    print(res)
