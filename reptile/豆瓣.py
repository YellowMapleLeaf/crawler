import requests
from bs4 import BeautifulSoup
import ssl


def craw(start,end):
    urls=[r'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}'.format(str(i)) for i in range(start,end,20)]

    # print(urls)
    for url in urls:

        data=requests.get(url)
        context = ssl._create_unverified_context()
        soup=BeautifulSoup(data.text,'lxml',context=context)
        # content > div > div.article > div > div.list-wp > div > a > div
        # div.list-wp > div.list > a.item > div.cover-wp > img
        # content > div > div.article > div > div.list-wp > div > a:nth-child(1) > div > img
        # content > div > div.article > div > div.list-wp > div > a:nth-child(1) > p
        # print(soup)
        # content > div > div.article > div > div.list-wp > div > a:nth-child(1) > div > img
        imgs=soup.select(r'content > div > div.article > div > div.list-wp > div > a > div > img')
        print(imgs)

craw(0,40)