import scrapy
from doubanTop.items import DoubantopItem


class doubanTopSpider(scrapy.Spider):
    name = "doubanTOP"

    start_urls=[
        'https://book.douban.com/top250'
    ]

    def parse(self, response):
        yield scrapy.Request(response.url,callback=self.bookTop)

        for page in response.xpath('//div[@class="paginator"]/a'):
            pageLink=page.xpath('@href').extract_first()
            # pageLink=response.urljoin(pageLink)
            yield  scrapy.Request(pageLink,callback=self.bookTop)


    def bookTop(self,response):
        for item in response.xpath('//tr[@class="item"]'):
            book=DoubantopItem()
            book['name']=item.xpath('td[2]/div[1]/a/@title').extract_first()
            book['content']=item.xpath('td[2]/p[1]/text()').extract_first()
            book['ratings']=item.xpath('td[2]/div[2]/span[2]/text()').extract()[0]
            yield book
