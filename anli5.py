alist=[]
def yazhan():
    print("输入要输入的值，按<end>结束")
    while True:
        a=input(">>")
        if a == 'end':
            break
        alist.append(a)
    return alist

def chuzhan():
    b=input("chuzhan:")
    if b in alist:
        chuzhan_1=alist.pop(alist.index(b))
        return chuzhan_1
    else:
        print("%s not in list" %b)
def chaxun():
    c=input("input what do you select:")
    if c not in alist:
        print("%s not in list" %c)
    else:
        chaxun_1=alist[alist.index(c)]
        print(chaxun_1)
    # return chaxun_1

memu='''(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择[0/1/2/3]:'''

if __name__=='__main__':
    while True:
        menu=input(memu)
        if menu == '0':
            yazhan()
            # print(alist)
        elif menu=='1':
            chuzhan()
        elif menu == '2':
            chaxun()
        else:
            break