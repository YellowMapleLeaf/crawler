import scrapy
from scrapyproject.items import QQnewItem
class QQnewSpider(scrapy.Spider):
    name="QQnewSpider"

    start_urls=['http://society.qq.com/']

    def parse(self, response):
        for new in response.xpath('//*[@id="news"]/div/div/div/div/em'):
            new_url=new.xpath("a/@href").extract_first()
            title=new.xpath('a/text()').extract_first()
            # print(title,new_url)
            # yield {"title":title,"new_url":new_url}
            new_url=response.urljoin(new_url)
            # print("******************")
            # print(new_url)
            yield scrapy.Request(new_url,callback=self.contentParse)

    # 解析新闻的内容
    def contentParse(self,response):
        title=response.xpath('/html/body/div/div/h1/text()').extract_first()
        # author=response.xpath('//*[@id="LeftTool"]/div/div/a/div/text()').extract_first()
        # year=response.xpath('//*[@id="LeftTool"]/div/div/span/text()').extract_first()
        # month=response.xpath('//*[@id="LeftTool"]/div/div/text()').extract_first()

        first_connent=response.xpath('/html/body/div/div/div/div/p[1]/text()').extract_first()
        # year=response.xpath('//*[@id="LeftTool"]/div/div[1]').extract_first()
        # month=response.xpath('//*[@id="LeftTool"]/div/div[2]').extract_first()
        # author=response.xpath('//*[@id="LeftTool"]/div/div[4]/a/div').extract_first()
        print(title)
        print('\n')
        print(first_connent)
        # print('\n')
        # print(year,month,author)
        print("***************\n")
        items=QQnewItem()
        items['new_title']=title
        items['new_content']=first_connent

