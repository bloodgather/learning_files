# -*- coding: utf-8 -*-
"""

课后习题3-2

"""

score = eval(input("百分制成绩："))

if score > 100:
    print("成绩有误")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score >= 0:
    print("E")
else:
    print("成绩有误")