#求任意数字区间的素数解法：
#lower = int(input("输入区间最小值: "))
#upper = int(input("输入区间最大值: "))
 
#for num in range(lower,upper + 1):
    # 素数大于 1
#    if num > 1:
#        for i in range(2,num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)


#求1000~5000以内的随机整数：
from random import *
listlong=[]
for i in range(1,21):
    num=randrange(1000,5000)
    listlong.append(num)
print(listlong)


# 求1~10之间素数：
list=[]
for num in range(1,11):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            list.append(num)
print(list)


#求listlong中不能被list中数整除的数：
number=[]

for num1 in listlong:
    if num1%2==0:        
        continue
    elif num1%3==0:
        continue
    elif num1%5==0:
        continue
    elif num1%7==0:
        continue
    else:
        number.append(num1)
print(number)




