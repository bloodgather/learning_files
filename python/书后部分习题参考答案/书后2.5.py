import math
import numpy
r1=eval(input("输入语文成绩："))
r2=eval(input("输入数学成绩："))
r3=eval(input("输入英语成绩："))
print("平均成绩：",math.fsum([r1,r2,r3])/3,"最高成绩：",max(r1,r2,r3),"最低成绩：",min(r1,r2,r3),"总评成绩：",0.5*r1+0.3*r2+0.2*r3)

#"总成绩：",math.fsum([r1,r2,r3]),
