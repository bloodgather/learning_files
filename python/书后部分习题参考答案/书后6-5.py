def see(x,lst):
    if min(lst)>=85:
        print(x)

def avg_total(x,lst):
    avg=sum(lst)/3
    total=sum(lst)
    print("{}的平均分为:{:.2f},总分为:{:.2f}".format(x,avg,total))
    return(avg,total)

def sortt(dict):
    lsVK=[(sum(v),k) for k,v in dict.items()]
    lsVK.sort()
    return lsVK

dict={'01':[67,88,45],'02':[97,68,85],'03':[97,98,95],'04':[67,48,45],'05':[82,58,75],'06':[96,49,65]}
for xuehao in dict:
    see(xuehao,dict[xuehao])

for xuehao in dict:
    avg_total(xuehao,dict[xuehao])

lsVK=sortt(dict)
dict_new = {}
for item in lsVK:
    dict_new[item[1]] = item[0]
print(dict_new)   
