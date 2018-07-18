for i in range(1,10):
    for  j in range(1,i+1):
        print("%s*%s=%s   "%(j,i,i*j),end='')
    print()
while 1:
    num=int(input("打印九九乘法表：请输入【1-9】之间的数值："))
    if num<=9:
        for i_1 in range(num,0,-1):
            for j_1 in range(1,i_1+1):
                print("%s*%s=%s   "%(j_1,i_1,i_1*j_1),end='')
            print()
        break
    else:print("错误输入，请输入【1-9】之间的数值。")


