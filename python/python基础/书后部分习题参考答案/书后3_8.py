# -*- coding: utf-8 -*-
"""

课后习题3-8

"""

import random

a = random.randint(1, 100)
b = random.randint(1, 100)
c = random.randint(1, 100)
print(a, b, c)

# method 1
for i in range(max(a,b,c), a * b * c + 1):
    if i % a == 0 and i % b == 0 and i % c == 0:
        break
print(i)

# method 2
m, n = a, b
while m % n != 0:
    m, n = n, m % n
t = a * b // n
m, n = t, c
while m % n != 0:
    m, n = n, m % n
print(t * c // n)