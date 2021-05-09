# -*- coding: utf-8 -*-
"""

课后习题 第五章 （3）

"""

# constant setting
n_total = 25
class1 = {"李雷", "张玉", "王晓刚", "陈红静", "方向", "司马清"}
class2 = {"施然", "李芳芳", "刘潇", "方向", "孙一航", "黄煌"}
class3 = {"陈红静", "方向", "刘培良", "张玉", "施小冉", "司马清"}

# problem 1
class_total = class1 | class2 | class3
print(25 - len(class_total))

# problem 2
two_class = ((class1 & class2) | (class1 & class3) | (class2 & class3))\
            - (class1 & class2 & class3)
print(two_class, len(two_class))

# problem 3
three_class = class1 & class2 & class3
print(three_class, len(three_class))

# problem 4
one_class = class_total - two_class - three_class
print(one_class, len(one_class))