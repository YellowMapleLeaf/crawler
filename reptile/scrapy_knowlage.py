
# 七月在线网页
# import scrapy
#
# class julyeduSpider(scrapy.Spider):
#     name="myfirstSpider"
#     start_urls=['https://www.julyedu.com/category/index']
#
#     def parse(self, response):
#         for julye in response.xpath('//*[@id="item_11"]/div'):
#             title=julye.xpath('div/a/h4/text()').extract_first()
#             print(title)
#             yield {'title':title}

#博客园
# import scrapy
#
# class cnblogSpider(scrapy.Spider):
#
#     name="cnblogSpider"
#
#     start_urls=[
#         'https://www.cnblogs.com/#p%s' %p for p in range(1,5)
#     ]
#
#     def parse(self, response):
#         print(self.start_urls)
#         for article in response.xpath('//div[@id="post_list"]/div[@class="post_item"]'):
#             title=article.xpath('div[@class="post_item_body"]/h3/a/text()').extract_first()
#             print(title)



import scrapy

class jokeSpider(scrapy.Spider):
    name = "jokeSpider"

    start_urls=[
        'http://quotes.toscrape.com/tag/humor/'
    ]

    def parse(self, response):
        for item in response.xpath('//div[@class="quote"]'):
            title=item.xpath('span[@class="text"]/text()').extract_first()
            yield {"title":title}
        #寻找下一页的链接，"@+属性名"获取属性值
        next_page=response.xpath('//li[@class="next"]/a/@href').extract_first()

        if next_page is not None:
            print(next_page)
            #urljoin能够将我们的找到的部分URL和原来的拼接起来，形成一个新的URL返回
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)

