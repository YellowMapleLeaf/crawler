# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#豆瓣TOP250本书
class DoubantopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()  # 书名
    price = scrapy.Field()  # 价格
    edition_year = scrapy.Field()  # 出版年份
    publisher = scrapy.Field()  # 出版社
    ratings = scrapy.Field()  # 评分
    author = scrapy.Field()  # 作者
    content = scrapy.Field()

#豆瓣评论
class DoubanCommentItem(scrapy.Item):
    useful_num = scrapy.Field()  # 多少人评论有用
    no_help_num = scrapy.Field()  # 多少人评论无用
    people = scrapy.Field()  # 评论者
    people_url = scrapy.Field()  # 评论者页面
    star = scrapy.Field()  # 评分
    comment = scrapy.Field()  # 评论
    title = scrapy.Field()  # 标题
    comment_page_url = scrapy.Field()  # 当前页

