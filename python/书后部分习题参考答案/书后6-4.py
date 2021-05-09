def avg(lst):
#    lst=[]
    return int(sum(lst)/len(lst))

dic={"小李":[77,54],"小张":[89,66,78,99],"小陈":[90],"小杨":[69,58,93]}
x=["","","",""]
y=[]
z=[]
lst=[]
i=0
j=0
for key in dic.keys():
    x[i]=key
    i+=1
print(x)

for value in dic.values():
    y.append(value)
print(y)

for k in range(0,4):
    y[k]=avg(y[k])
print(y)

new_list= [[x[0],y[0]],[x[1],y[1]],[x[2],y[2]],[x[3],y[3]]]
#dict(new_list)
print(new_list)
dict={}
for item in new_list:
    dict[item[0]] = item[1]
print(dict)
