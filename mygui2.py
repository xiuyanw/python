import tkinter
from functools import partial


def hello():
    def welcom():
        lb.config(text="hello tedu!!!")
    return welcom  #hello函数的返回值还是一个函数，这就是毕包。

root= tkinter.Tk()
lb =tkinter.Label(text="Hello World!",font='Times 26')
MyBtn=partial(tkinter.Button,root,fg='White',bg='blue')
b1=MyBtn(text='Button1',command=hello('China!!'))
b2=MyBtn(text='Button2',command=hello("tedu!!"))
b3=MyBtn(text='Quit',command=root.quit)
lb.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()