def gen_fib(l):  #l为形参
    fib=[0,1]
    # l=int(input("please input a number:"))  参数的来源不一定是键盘输入，也可能是来源于文件。所以用传参的方式
    for i in range(l-len(fib)):
        fib.append(fib[-1]+fib[-2])
    return fib


print(gen_fib(10))   #10为实参
print('-'*50)
n=int(input("please input a number:"))
a=gen_fib(n)  #不会把变量n传入，是把n代表的值赋值给形参
print(a)