# import urllib.request
#
#
# header={
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
# }
#
# req=urllib.request.Request(r'http://www.baidu.com',headers=header)
#
# response=urllib.request.urlopen(req)
#
#
# data=response.read().decode("utf-8")
# print(data)



import urllib.request
import random

AgentList=[
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"
]

#从浏览器信息列表中取出一条
agent=random.choice(AgentList)

req=urllib.request.Request(r"http://www.baidu.com")

req.add_header("User-Agent",agent)

response=urllib.request.urlopen(req)

data=response.read().decode("utf-8")

print(data)





