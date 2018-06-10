
import os

def getDirAll(path):
    #获取路径下的所有文件
    fileList=os.listdir(path)

    for file in fileList:
        absPath = os.path.join(path, file)
        print(absPath)
        if os.path.isdir(absPath):
            getDirAll(absPath)
            print("目录：%s"%absPath)
        else:
            print("文件：%s" % absPath)


filePath=r'H:\软件'
getDirAll(filePath)









