import tkinter

def writeText():
    msg=""
    if Moneychioce.get():
        msg+="money\n"
    if Powerchioce.get():
        msg+="power\n"
    if Hobbychioce.get():
        msg+="hobby\n"
    text.delete(0.0,tkinter.END)
    text.insert(tkinter.INSERT,msg)

win=tkinter.Tk()

#variable绑定变量
Moneychioce=tkinter.BooleanVar()
MoneyCheckButton=tkinter.Checkbutton(win,text="money",variable=Moneychioce,command=writeText)
MoneyCheckButton.pack()
Powerchioce=tkinter.BooleanVar()
PowerCheckButton=tkinter.Checkbutton(win,text="power",variable=Powerchioce,command=writeText)
PowerCheckButton.pack()
Hobbychioce=tkinter.BooleanVar()
HobbyCheckButton=tkinter.Checkbutton(win,text="hobby",variable=Hobbychioce,command=writeText)
HobbyCheckButton.pack()


text=tkinter.Text(win)
text.pack()


win.mainloop()






