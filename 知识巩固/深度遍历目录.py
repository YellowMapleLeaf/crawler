import os


def getAllFileDE(path):
    statck=[]
    statck.append(path)

    while len(statck)!=0:
        targetFile=statck.pop()

        #获取目录下的文件
        fileList=os.listdir(targetFile)

        for file in fileList:
            absPath=os.path.join(targetFile,file)
            if os.path.isdir(absPath):
                statck.append(absPath)
                print("目录：%s" % absPath)
            else:
                print("文件：%s" % absPath)


filePath=r'H:\软件'
getAllFileDE(filePath)






