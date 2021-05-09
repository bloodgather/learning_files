sentence=input("请输入一句英文句子：")
LL=len(sentence)
length=[0,0,0,0,0,0,0,0,0,0]
sentencelist=[]
sentencelist=sentence.split()
print(sentencelist)
#for i in range(1,LL):

x0=len(sentencelist[0])
x1=len(sentencelist[1])
x2=len(sentencelist[2])
x3=len(sentencelist[3])
x4=len(sentencelist[4])
print(x0,x1,x2,x3,x4)

for i in range(10):
    length[i]=len(sentencelist[i])
print(length)
print(max(length))
