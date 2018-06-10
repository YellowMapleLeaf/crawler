import scrapy
#构造虚拟代理
from faker import Factory
f = Factory.create()

class commentSpider(scrapy.Spider):
    name = "doubanCommentSpider"

    start_urls=[
        'https://www.douban.com/'
    ]

    #构造请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Host': 'accounts.douban.com',
        'User-Agent': f.user_agent()
    }


    #构造表单数据
    formdata={

    }