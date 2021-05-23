list=[["王平","男",1,1,0,0],["李丽","女",0,1,0,1],["陈小梅","女",0,0,1,0],["孙洪涛","男",0,1,1,1],["方亮","男",1,0,1,0]]
situation=[]
situation2=[]

#报名超过两项（含两项）的学生人数
scores=[item[2:] for item in list]
totals=[sum(item) for item in scores]

k=0
for i in range(5):
    if totals[i]>=2:
        k=k+1
print("报名项目超过两项的学生人数",k)

#输出女生的报名情况
sex=[item[1] for item in list]
for j in range(5):
    if sex[j]=='女':
         situation.append(list[j])
print("女生情况有:",situation)
        
#输出所有报名参加3000m的学生姓名和性别
Competition=[item[3] for item in list]
material=[item[0:1] for item in list]
for i in range(5):
    if Competition[i]==1:
        situation2.append(material[i])
print("所有报名参加3000m的学生有:",situation2)
