import win32com
import win32com.client
import os

def createWord(path,name):
    wm=win32com.client.Dispatch("Word.Application")
    #让文档可见
    wm.Visible=True
    #创建word文档
    doc=wm.Documents.Add()

    #开始写内容,从头开始写
    r=doc.Range(0,0)
    r.InsertAfter("亲爱的"+name+":\n")
    r.InsertAfter("我一定不会辜负你的~")

    doc.SaveAs(path)
    doc.Close()
    wm.Quit()

nameList=['张三','李四','王五']

for name in nameList:
    createWord(os.path.join(os.getcwd(),name),name)












