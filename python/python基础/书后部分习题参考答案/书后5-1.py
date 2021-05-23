dicTXL={'小新':{'手机':13913000001, 'QQ号':18191220001}, '小亮': {'手机':13913000002,'QQ号':18191220002}, '小刚': {'手机':13913000003,'QQ号':18191220003}}
dicOther={"大刘":{'手机':13914000001,'QQ号':18191230001},"大王":{'手机':13914000002,'QQ号':18191230002},"大张":{'手机':13914000003,'QQ号':18191230003}}
dicWX={'小新':'xx9907','小刚':'gang1004','大王':'jack_w','大刘':'liu666'}
dicAll={}

#合并：
for k,v in dicOther.items():
    dicTXL[k]=v
print(dicTXL)

#增加：
for key in dicWX.keys():
    for key in dicTXL.keys():
        dicAll[key]=dicTXL.get(key),dicWX.get(key)
    dicAll[key]=dicTXL.get(key),dicTXL['手机']
       
print(dicAll)
