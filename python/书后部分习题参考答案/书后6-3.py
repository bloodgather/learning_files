#def avg(a,b,c):
#    return int((a+b+c)/3)

#s={'小李':[77,54,57],'小张':[89,66,78],'小陈':[90,93,80],'小杨':[69,58,93]}
#x=int(input("第一门课程的成绩："))
#y=int(input("第二门课程的成绩："))
#z=int(input("第三门课程的成绩："))
#sum=avg(x,y,z)
#print(sum)


def avg(a,b,c):
    return int((a+b+c)/3)

dic={'小李':[77,54,57],'小张':[89,66,78],'小陈':[90,93,80],'小杨':[69,58,93]}
i,j=0,0
x=['','','','']
y=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
for key in dic.keys():
    x[i]=key
    i+=1
print(x)
for value in dic.values():
    y[j]=value
    j+=1
print(y)
for k in range(0,4):
    y[k]=avg(y[k][0],y[k][1],y[k][2])
print(y)

new_list= [[x[0],y[0]],[x[1],y[1]],[x[2],y[2]],[x[3],y[3]]]
dict(new_list)
dict={}
for item in new_list:
    dict[item[0]] = item[1]
print(dict)

