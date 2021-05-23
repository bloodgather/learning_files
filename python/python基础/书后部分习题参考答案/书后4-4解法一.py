sentence=input("请输入一句英文句子：")
LL=len(sentence)
length=[0,0,0,0,0,0,0,0,0,0]
sentencelist=[]
sentencelist=sentence.split()
print(sentencelist)

for i in range(LL):
    length[i]=len(sentencelist[i])
print(length)
print(max(length))
