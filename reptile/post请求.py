import urllib.request
import ssl
import urllib.parse

url=r'http:\\www.baidu.com'
data = {
    "username":"sunck",
    "passwd":"666"
}
postData=urllib.parse.urlencode(data).decode("utf-8")

req=urllib.request.Request(url)

req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0')

reponse=urllib.request.urlopen(req)

reponse.read().decode("utf-8")





