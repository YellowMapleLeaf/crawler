from collections import OrderedDict


from pyexcel_xls import save_data

def writeXls(path,data):
    dic=OrderedDict()
    for sheetName,sheetData in data.items():
        # d={}
        dic[sheetName]=sheetData

    save_data(path,dic)


path=r'C:\Users\User\Desktop\杂类文件\writeXls.xls'
data={'表1':[[1,2,3],[4,5,6],[7,8,9]],
      '表2':[[11,22,33,44],[55,66,77,88,99,00]]}
writeXls(path,data)






