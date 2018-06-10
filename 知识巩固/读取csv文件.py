import csv


def readCsv(path):
    csvList=[]
    with open(path,"r") as csvFile:
        #读取csv文件到csvData中
        csvData=csv.reader(csvFile)
        for line in csvData:
            csvList.append(line)
    return csvList




path=r""
readCsv(path)
