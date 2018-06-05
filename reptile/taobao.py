from selenium import webdriver
import time


browser=webdriver.Chrome()

browser.set_page_load_timeout(30)

browser.get('https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306')

page_info=browser.find_element_by_css_selector('#mainsrp-pager > div > div > div > div.total').text

pages=int(page_info.split(' ')[1])
print(pages)

# for page in pages:
#     if page >2:
#         break
url='https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=4&p4ppushleft=%2C48&s=88&ntoffset=4'

browser.get(url)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)   # 不然会load不完整

goods=browser.find_element_by_css_selector(r'#mainsrp-itemlist > div > div > div:nth-child(1)').find_elements_by_tag_name('div')


for good in goods:
    title=good.find('#J_Itemlist_TLink_567293908632').text
    print(title)


'''
https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=4&p4ppushleft=%2C48&s=44&ntoffset=4
https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&bcoffset=4&p4ppushleft=%2C48&s=88&ntoffset=4
'''
