# import urllib.request
# import ssl
# import json
#
# def ajaxCrawler(url):
#     header={
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
#     }
#     context=ssl._create_unverified_context()
#     req=urllib.request.Request(url,headers=header)
#     response=urllib.request.urlopen(req,context=context)
#     jsonStr = response.read().decode("utf-8")
#     jsonData=json.loads(jsonStr)
#     return jsonData
#
#
# urls=[r'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}'.format(str(i)) for i in range(start,end,20)]
#
# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20"
# info = ajaxCrawler(url)
# print(len(info))
#
#
#

import urllib.request
import ssl
import json
import re

def ajaxCrawler(urls):
    header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    context=ssl._create_unverified_context()
    for url in urls:
        req=urllib.request.Request(url,headers=header)
        response=urllib.request.urlopen(req,context=context)
        data=response.read().decode("utf-8")
        reImg = r'<div class="cover-wp" .*>'
        reObject = re.compile(reImg)
        imgList = reObject.findall(data)
        print(imgList)



urls=[r'https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}'.format(str(i)) for i in range(0,40,20)]

info = ajaxCrawler(urls)












