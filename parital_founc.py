
#yum install sqlite-devel tcl-devel tk-devel -y
#./configure --prefix=/usr/local
#make && make install
from functools import partial
import tkinter
root=tkinter.Tk()
# def foo(a,b,c,e,f):
#     return a+b+c+e+f
#
# if __name__ == '__main__':
#     print(foo(10,20,30,40,50))
#     print(foo(10,20,30,40,25))
#     add=partial(foo,10,20,30,40) #相当于把前面的4个参数都固定下来了。
#     print(add(f=5))   #只需要给剩下的参数赋值。
#     print(add(f=12))
#     print(add(10))