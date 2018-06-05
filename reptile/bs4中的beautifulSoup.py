from bs4 import BeautifulSoup
import requests

# title=['t1','t2','t3','t4']
# img=['i1','i2','i3','i4']
# rates=['r1','r2','r3','r4']
#
# i=0
# for title,img,rates in zip(title,img,rates):
#     data={
#         'title':title,
#         'img':img,
#         'rates':rates
#     }
#     print(data)

# https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#FILTERED_LIST
urls=[r'https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#FILTERED_LIST'.format(str(i)) for i in range(30,900,30)]
print(urls)
for url in urls:
    wd_data = requests.get(url)
    soup = BeautifulSoup(wd_data.text, 'lxml')
    titles=soup.select(r'div.listing > div.listing_details > div.listing_info > div.listing_title > a')
    for title in titles:
        print(title.get_text())




# content用于获取图片，返回二进制数据
# text用于获取内容，返回的是unicode解码字符串

# wd_data=requests.get(url)
# soup=BeautifulSoup(wd_data.text,'lxml')
# #taplc_attraction_coverpage_attraction_0 > div:nth-child(3) > div > div > div.shelf_item_container > div:nth-child(1) > div.poi > div > div.item.name > a
# #ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.listing_info > div.listing_title > a
# titles=soup.select(r'div.listing > div.listing_details > div.listing_info > div.listing_title > a')
# #ATTR_ENTRY_ > div.attraction_clarity_cell > div > div > div.photo_booking.non_generic > a
# imgs=soup.select(r' div.attraction_clarity_cell > div > div > div.photo_booking.non_generic > a > img')
# # print(imgs)
#
# for title in titles:
#     print(title.get_text())
#
# # print(len(title),len(img))
# # for title,img in zip(title,img):
# #     data={
# #         'title':title,
# #         'img':img
# #     }
# #     print(data)
#
# # print(img)

















