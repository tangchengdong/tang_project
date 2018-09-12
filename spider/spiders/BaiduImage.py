# -*- coding: utf-8 -*-
import scrapy,os
import json
import requests


class ImageSpider(scrapy.Spider):
    name = 'image'
    # allowed_domains = ['baidu.com']
    input_name=input("输入：")
    pn = 0
    start_urls = []
    try:
        os.mkdir("./baidu/%s"%input_name)
    except:
        pass
    num = 1
    while pn < 200:
        urls = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&word={}&pn={}'.format(input_name,pn)
        start_urls.append(urls)
        pn+=30

    def parse(self, response):
        try:
            response=response.body.decode("utf-8")
            a=json.loads(response)["data"]
        except:
            pass

        headers = {
            'Cookie': 'BDqhfp=%E5%90%A7%E4%B8%A2%26%260-10-1undefined%26%260%26%261; BAIDUID=6482109882697A4DB822E0791AEB74CC:FG=1; PSTM=1512473029; BIDUPSID=02A83A33F13CFCDB22BB94ED3EE00DB7; MCITY=-340%3A; BDUSS=XBKcGdrdTJaa0xCZ1JxQk1UbkJRRjlZQjZRNnY5YjJNQUpOaUlOQWVVNEcyR0ZhQVFBQUFBJCQAAAAAAAAAAAEAAAC0dZI0uePW3TIwMTQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZLOloGSzpae; BDRCVFR[S_ukKV6dOkf]=mk3SLVN4HKm; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; firstShowTip=1; indexPageSugList=%5B%22%E5%90%A7%E4%B8%A2%22%5D; cleanHistoryStatus=0; userFrom=null; PSINO=1; H_PS_PSSID=1466_21112_25177',
            # 'Referer': 'https://image.baidu.com/search/index?ct=201326592&z=9&tn=baiduimage&word=%E9%A3%8E%E6%99%AF&pn=0&ie=utf-8&oe=utf-8&cl=2&lm=-1&fr=ala',

        }
        # print(type(a))

        for i in a:

            try:
                url=i["thumbURL"]
                response = requests.get(url, headers=headers, timeout = 1)
                # self.jpg(response)
                self.num += 1
            except:
                pass



    def jpg(self,response):
        with open("./baidu/%s/%s.jpg"%(self.input_name,self.num), 'wb') as f:
            f.write(response.content)



