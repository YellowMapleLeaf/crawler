import urllib.request


url=r'http://www.baidu.com'
#编码
url2=urllib.request.quote(url)
print(url2)
#解码
url3=urllib.request.unquote(url2)
print(url3)

#向指定服务器发送请求
response=urllib.request.urlopen(url3)

#读取全部的数据
# data=response.read().decode("utf-8")
# print(data)

#获得相关信息
print(response.info())

#返回状态码
print(response.getcode())

#返回正在爬取得URL
print(response.geturl())


# 读取一行
#data = response.readline()

#读取文件的全部内容，会把读取到的数据赋值给一个列表变量
#data = response.readlines()




