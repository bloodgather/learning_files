# -*- coding: utf-8 -*-
"""

课后习题3-6

"""

n = eval(input("请输入正整数："))

if n < 17:
    print("无解")
else:
    print(n // 17 * 17)