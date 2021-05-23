import math
def area(r):
  
    s=math.pi*r*r
    return s

print("半径为3.5的面积为：{:.2f}".format(area(3.5)),end=',')
print("半径为2.9的面积为：{:.2f}".format(area(2.9)),end=',')
xx=area(6.2)-area(3.3)
print("外圆半径6.2，內圆半径3.3的面积为：{:.2f}".format(xx))
