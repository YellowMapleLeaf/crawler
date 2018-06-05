import urllib.request
import os
import re


def imgReptile(path,toPath):
    header={
        'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"
    }
    req=urllib.request.Request(path,headers=header)

    response=urllib.request.urlopen(req)
    data=response.read().decode("utf-8")

    # print(type(data))

    # with open("close2.html",'w',encoding="utf-8") as file:
    #     file.write(data)
# <img width="88" height="35" src="//img30.360buyimg.com/popshop/jfs/t2590/347/2539990180/32834/96cc17e6/576b8c57N60f75b94.jpg" />
#<img src="//img10.360buyimg.com/n7/s230x322_jfs/t18016/351/2259872343/96388/3b232874/5aec2131Nba7a3aff.jpg!cc_230x322.jpg"/>
#<img original="//img14.360buyimg.com/n7/s230x322_jfs/t19792/19/1748523971/187838/9119e5/5ad558f6N35e3dd02.jpg!cc_230x322.jpg" />
#     reImg=r'<img width="88" height="35" src="//(.*)" />'
#     reImg = r'<img original="//(.*?)"(.*?){0,} />'
#     reImg = r'<img original="//(.*?)"(.*?){0,} />'
    reImg = r'<img src="//(.*?)".*/>'
    reObject=re.compile(reImg)
    imgList=reObject.findall(data)
    print(len(imgList))
    print(imgList)
    # num = 1
    # for imageUrl in imgList:
    #     imgPath = os.path.join(toPath, str(num)+".jpg")
    #     num += 1
    #     #把图片下载到本地存储
    #     urllib.request.urlretrieve("http://"+imageUrl, filename=imgPath)


path=r'http://search.yhd.com/c0-0/k%25E5%25A5%25B3%25E8%25A3%2585/'
toPath=r'H:\python编程\reptile\img'

imgReptile(path,toPath)










