import scrapy
#构造虚拟代理
from faker import Factory
from urllib import parse
from doubanTop.items import DoubanCommentItem
f = Factory.create()

class commentSpider(scrapy.Spider):
    name = "doubanCommentSpider"

    start_urls=[
        'https://www.douban.com/'
    ]

    #构造请求头
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Host': 'accounts.douban.com',
        'User-Agent': f.user_agent()
    }


    #构造表单数据
    formdata={
        'form_email': '17746913064',
        'form_password': 'cgz12345678',
        # 'captcha-solution': '',
        # 'captcha-id': '',
        'login': '登录',
        'redir': 'https://www.douban.com/',
        'source': 'index_nav'
    }

    ####################################################
    #  name         : start_requests
    #  function     : 爬虫启动时，会首先执行start_requests函数的调用，执行成功之后，再去执行parse()函数进行解析
    #                  发送登录豆瓣的请求
    #  parameters_in:
    #
    #  parameters_out:
    #               scrapy.Request:请求登录
    ####################################################
    def start_requests(self):
        return [scrapy.Request(url='https://www.douban.com/accounts/login',
                              headers=self.headers,
                              meta={'cookiejar': 1},
                              callback=self.loginParse)]

    ####################################################
    #  name         : loginParse
    #  function     : 处理验证码
    #  parameters_in:
    #               response:
    #  parameters_out:
    #               scrapy.FormRequest.from_response:提交表单的登录信息
    ####################################################
    def loginParse(self,response):
        if b'captcha_image' in response.body:
           link=response.xpath('//img[@class="captcha_image"]/@src').extract()[0]
           print(link)
           captcha_solution=input('请输入验证码：')
           captcha_id=parse.parse_qs(parse.urlparse(link).query,True)['id']
           self.formdata['captcha-solution']=captcha_solution
           self.formdata['captcha-id'] = captcha_id
        #提交表单信息
        return [scrapy.FormRequest.from_response(response,
                                                 headers=self.headers,
                                                 formdata=self.formdata,
                                                 meta={'cookiejar':response.meta['cookiejar']},
                                                 callback=self.afterLogin
                                                 )]
    ####################################################
    #  name         : afterLogin
    #  function     : 成功登录之后，开始爬取网页的数据
    #  parameters_in:
    #               response:
    #  parameters_out:
    #
    ####################################################
    def afterLogin(self,response):
        print(response.status)
        self.headers['Host']='www.douban.com'
        yield scrapy.Request(url='https://movie.douban.com/subject/22266320/reviews',
                             headers=self.headers,
                             meta={'cookiejar':response.meta['cookiejar']},
                             callback=self.commentUrlParse,
                             dont_filter=True)
        yield scrapy.Request(url='https://movie.douban.com/subject/22266320/reviews',
                             headers=self.headers,
                             meta={'cookiejar':response.meta['cookiejar']},
                             callback=self.nextpageParse,
                             dont_filter=True)
    ####################################################
    #  name         : commentUrlParse
    #  function     : 爬取评论的链接
    #  parameters_in:
    #               response:
    #  parameters_out:
    #
    ####################################################
    def commentUrlParse(self,response):
        for item in response.xpath('//div[@class="main review-item"]/div[1]/h2'):
            commentUrl=item.xpath('a/@href').extract_first()
            commentTitle=item.xpath('a/text()').extract_first()
            # print("*************")
            # print(commentTitle,commentUrl)
            yield scrapy.Request(commentUrl,
                                 headers=self.headers,
                                 meta={'cookiejar': response.meta['cookiejar']},
                                 callback=self.commentParse
            )
    ####################################################
    #  name         : commentParse
    #  function     : 爬取评论
    #  parameters_in:
    #               response:
    #  parameters_out:
    #
    ####################################################
    def commentParse(self,response):
        content=response.xpath('//header[@class="main-hd"]')
        authorUrl=content.xpath('a/@href').extract_first()
        author=content.xpath('a/span/text()').extract_first()
        print(author,authorUrl)


    ####################################################
    #  name         : nextpageParse
    #  function     : 爬取评论下一页
    #  parameters_in:
    #               response:
    #  parameters_out:
    #
    ####################################################
    def nextpageParse(self,response):
        try:
            nextPage=response.xpath('//span[@class="next"]/a/@href').extract()[0]
            nextPage=response.urljoin(nextPage)
            print("****************************下一页：")
            print(nextPage)
            yield scrapy.Request(url=nextPage,
                                 headers=self.headers,
                                 meta={"cookiejar":response.meta['cookiejar']},
                                 callback=self.commentUrlParse,
                                 dont_filter=True)      #默认去重，必须加这个，不去重
            yield scrapy.Request(url=nextPage,
                                 headers=self.headers,
                                 meta={"cookiejar":response.meta['cookiejar']},
                                 callback=self.nextpageParse,
                                 dont_filter=True)
        except:
            print("Error:no page")
            return



