# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QQnewItem(scrapy.Item):
    # 新闻的标题
    new_title = scrapy.Field()
    # 新闻的内容
    new_content = scrapy.Field()

