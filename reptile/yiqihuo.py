from selenium import webdriver
import time

#用谷歌浏览器
browers=webdriver.Chrome()

#设置超时时间
browers.set_page_load_timeout(30)

browers.get('http://www.17huo.com/search.html?sq=2&keyword=%E7%BE%8A%E6%AF%9B')

page_info=browers.find_element_by_css_selector('body > div.wrap > div.pagem.product_list_pager > div').text

pages=int((page_info.split('，')[0]).split(' ')[1])

for page in range(pages):
    if page>2:
        break
    url=r'http://www.17huo.com/?mod=search&sq=2&keyword=%E7%BE%8A%E6%AF%9B&page='+ str(page)
    #爬取该网页
    browers.get(url)

    #执行一下script代码,滚动滚动条到末尾
    browers.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    time.sleep(3)

    #寻找一个页面内容的所有商品
    goods=browers.find_element_by_css_selector('body > div.wrap > div:nth-child(2) > div.p_main > ul').find_elements_by_tag_name('li')

    for good in goods:
        try:
            title=good.find_element_by_css_selector('a:nth-child(1) > p:nth-child(2)').text
            price=good.find_element_by_css_selector('div > a > span').text
            print(title,price)
        except:
            print(good.text)










