import tkinter


def func():
    print(username.get(),passwd.get())

#创建一个主窗口
win=tkinter.Tk()
#设置窗口标题
win.title("pythonGUI")
#设置窗口大小
win.geometry("450x500")

#创建标签，可以显示文本的
label=tkinter.Label(win,
                    bg="green",
                    text="这是Lable")

#显示标签
label.pack()

#滚动条
scroll=tkinter.Scrollbar()

#创建文本控件,多行文本
#height:显示的行数
text=tkinter.Text(win,
                  height=2,
                  width=30)

scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text.pack(side=tkinter.LEFT,fill=tkinter.Y)


#关联text和scroll
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)


str="""
    dfghserygh 34etyirejyt34ioepjtg54y56u675ujhgjnghcvhsrhtrh
    wertgeryttertetret
    rthrtyjyrtyt
    """
text.insert(tkinter.INSERT,str)

#创建按钮
button=tkinter.Button(win,text="按钮",command=func)
button.pack()
button1=tkinter.Button(win,text="退出",command=win.quit)
button1.pack()

#取输入控件输入的需要先创建一个变量，然后绑定
username=tkinter.Variable()
passwd=tkinter.Variable()

#输入控件
entry=tkinter.Entry(win,
                    textvariable=username)
entry.pack()
#show，密文显示
entry1=tkinter.Entry(win,show="*",
                     textvariable=passwd)
entry1.pack()


win.mainloop()