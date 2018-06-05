import urllib.request

urllib.request.urlretrieve(r'http://www.baidu.com',filename='baidu.html')

#上面这个方法会产生一些缓存，可以调用下面的函数清除缓存
urllib.request.urlcleanup()
