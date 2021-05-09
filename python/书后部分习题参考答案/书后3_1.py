# -*- coding: utf-8 -*-
"""

课后习题 3(1)

"""

n = eval(input("请输入待面试人数："))

for i in range(n):
    ids = eval(input("序号："))
    age = eval(input("年龄："))
    exp = eval(input("工作经验/年："))
    maj = input("所学专业：")
    if (maj == "计算机" and age < 25) or\
       (maj == "电子" and exp > 4) or\
       (maj == "通信"):
        print("获得面试机会")
    else:
        print("抱歉，您不符合面试条件")