import requests
from PIL import Image
from io import BytesIO

#
# url='https://img02.sogoucdn.com/app/a/100520024/4220078f72de3e9b8b5a9503d602c9fe'
# imageData=requests.get(url)
# img=Image.open(BytesIO(imageData.content))
# img.save('1.jpg')


url='http://www.baidu.com'
data=requests.get(url)
cookies=data.cookies.get_dict()
print(cookies)






