def showMsg():
    print("Happy birthday to you!"*n)
def showMsgB(name):
    showMsg()
    print("Happy birthday, dear {}!".format(name))

name=input("请输入姓名:")
n=int(input("请输入n的值:"))
if name!="小明":
    showMsg()
else:
    showMsgB("小明")
    print("Happy birthday to you!")
