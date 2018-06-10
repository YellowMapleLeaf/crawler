#导入有序字典
from collections import OrderedDict

#用来去xls和xlsx文件的数据
from pyexcel_xls import get_data


def readXlsAndXlsx(path):
    dic=OrderedDict()
    xdata=get_data(path)
    for sheet in xdata:
        dic[sheet]=xdata[sheet]
    return dic


path=r'C:\Users\User\Desktop\杂类文件\2016-2017学年国家励志奖学金汇总表.xlsx'
Odic=readXlsAndXlsx(path)
print(Odic)