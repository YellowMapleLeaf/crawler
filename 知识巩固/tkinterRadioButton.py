import tkinter

def func():
    if choice.get():
        print(choice.get())

win=tkinter.Tk()

choice=tkinter.IntVar()

MoneyRadiobutton=tkinter.Radiobutton(win,text="money",variable=choice,value=1,command=func)
MoneyRadiobutton.pack()
PowerRadiobutton=tkinter.Radiobutton(win,text="power",variable=choice,value=2,command=func)
PowerRadiobutton.pack()
HobbyRadiobutton=tkinter.Radiobutton(win,text="hobby",variable=choice,value=3,command=func)
HobbyRadiobutton.pack()

win.mainloop()










