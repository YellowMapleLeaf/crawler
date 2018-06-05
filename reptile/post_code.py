import requests
import xml.etree.ElementTree as ET
#创建一个XML的分析器
from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def __init__(self,provices):
        self.provices=provices

    #开始的时候,获取某节点名称及属性值集合
    def start_element(self,name, attrs):
        if name!='map':
            name=attrs['title']
            href=attrs['href']
            self.provices.append((name,href))

    #结束的时候,获取某节点结束名称
    def end_element(self,name):
        pass

    #中间节点的值
    def char_data(self,text):
        pass




def get_province_post(url):
    content=requests.get(url).content.decode("gb2312")

    start=content.find(r'<map name="map_86" id="map_86">')
    end=content.find(r'</map>')
    content=content[start:end+len(r'</map>')]
    provices=[]
    handler=DefaultSaxHandler(provices)
    parser=ParserCreate()
    parser.StartElementHandler=handler.start_element
    parser.EndElementHandler=handler.end_element
    parser.CharacterDataHandler=handler.char_data
    # 解析数据
    parser.Parse(content)
    # 结果字典为每一页的入口代码
    return provices

url=r'http://www.ip138.com/post/'
provices=get_province_post(url)
print(provices)