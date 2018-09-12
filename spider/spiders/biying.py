# -*- coding: utf-8 -*-

import re
import scrapy
from spider.items import BiyingItem
from scrapy import signals


class bingying(scrapy.Spider):

    # 爬虫名称
    name = 'by'
    start_urls=['https://bing.ioliu.cn/']

    # 设置
    custom_settings = {
        'ROBOTSTXT_OBEY': False,

        # 请求操时，默认时180s
        # 'DOWNLOAD_TIMEOUT':180,

        # 请求等待时间
        # 'DOWNLOAD_DELAY': 3,

        # 更改线程数
        # 'CONCURRENT_REQUESTS': 32

        # 请求headers设置
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en',
            'referer': 'https://bing.ioliu.cn/',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        },

        # 管道中间键
        'ITEM_PIPELINES': {
           'spider.pipelines.BiyingPipeline': 300,
        },

    }
    # @classmethod
    # def from_crawler(cls, crawler, *args, **kwargs):
    #     spider = cls(*args, **kwargs)
    #     spider._set_crawler(crawler)
    #     return spider

    def parse(self, response):
        node_list = response.xpath('//div[@class="item"]')
        for node in node_list:
            item = BiyingItem()
            item['url'] ='https://bing.ioliu.cn'+ node.xpath('./div/div[@class="options"]/a[@class="ctrl download"]/@href').extract_first()
            yield item
            # url = node.xpath('./div/div[@class="options"]/a[@class="ctrl download"]/@href').extract_first()
            # yield response.follow(url, callback=self.parse_ma, dont_filter=True)
        try:
            next_url =response.xpath('//div[@class="page"]/a/@href').extract()[1]
            next_url_x = re.findall(r'=(.*)', next_url)[0].strip()
            end_url = response.xpath('//div[@class="page"]/span/text()').extract_first()
            end_url = re.findall(r'/(.*)', end_url)[0].strip()
            if next_url_x == end_url:
                return
            else:
                yield response.follow(next_url, callback=self.parse)

        except:
            pass
        # yield response.follow(next_url, callback=self.parse)
    # def parse_ma(self, response):
        # print(response.url)
        # yield

        # print(response.url)
        # with open('美图.jpg', 'wb') as f:
        #     f.write(response.body)