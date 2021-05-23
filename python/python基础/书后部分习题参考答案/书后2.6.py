import math
r=eval(input("请输入一个3位数："))
      
r100=r//100
r10=r%100
r101=r10//10
r=r10%10
x=r100+r101+r
print(x)
