import requests
from bs4 import BeautifulSoup


url=r'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#FILTERED_LIST'

header={
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
}

data=requests.get(url,headers=header)

textData=BeautifulSoup(data.text,'lxml')
#a105123 > div.thumb.thumbLLR.soThumb
#'div.listing whiteList divider > div.thumb thumbLLR soThumb > img '
imgs=textData.select('div.thumb.thumbLLR.soThumb > img')

for img in imgs:
    print(img.get('src'))


