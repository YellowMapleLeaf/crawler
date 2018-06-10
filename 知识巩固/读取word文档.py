import win32com
import win32com.client


def readWord(path,toPath):
    #调用系统的word功能，可以处理doc和docx
    wordManager=win32com.client.Dispatch("Word.Application")
    #打开文件
    doc=wordManager.Documents.Open(path)
    #写入另一个word文档中
    doc.SaveAs(toPath, 2)

    # for paragraph in doc.Paragraphs:
    #     line=paragraph.Range.Text
    #     print(line)

    doc.Close()
    wordManager.Quit()


path=r'C:\Users\User\Desktop\杂类文件\入侵检测论文.doc'
toPath="a.txt"

readWord(path,toPath)




