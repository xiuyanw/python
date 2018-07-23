import tkinter
from functools import partial
root= tkinter.Tk()
lb =tkinter.Label(text="Hello World!")
b1=tkinter.Button(root,fg='White',bg='blue',text='Button1')
MyBtn=partial(tkinter.Button,root,fg='White',bg='blue')
b2=MyBtn(text='Button 2')
b3=MyBtn(text='Quit',command=root.quit)
lb.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()

