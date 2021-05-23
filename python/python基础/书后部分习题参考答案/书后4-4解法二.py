sentence=input("请输入一句英文句子：")
length=[]
#sentencelist=[]
sentencelist=sentence.split()
LL=len(sentencelist)

for i in range(LL):
    
    x=len(sentencelist[i])
        
    length.append(x)
    
print(length)
print(max(length))
