import requests
from lxml import etree
request=requests.Session()

for i in range(0,251,25):
    if i > 20:
        break
    url='https://movie.douban.com/top250?start='+str(i)+'&filter='
    data=request.get(url)
    data.encoding = 'utf-8'
    root=etree.HTML(data.content)
    items=root.xpath('//ol/li/div[@class="item"]')
    for item in items:
        title=item.xpath('./div[@class="info"]//a/span[@class="title"]/text()')[0]
        print(title)

