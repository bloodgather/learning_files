def avg(lst):
    return int(sum(lst)/len(lst))

dic={"小李":[77,54],"小张":[89,66,78,99],"小陈":[90],"小杨":[69,58,93]}

for name in dic:
    dic[name] = avg(dic[name])

print(dic)
