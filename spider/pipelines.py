# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd
import numpy as np
from core.data.db.biying import Biying
import requests
import re

class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class BiyingPipeline(object):

    def __init__(self):
        self.table = Biying()
        self.heardes = {
            'referer': 'https://bing.ioliu.cn/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        }

    def process_item(self, item, spider):
        # print(dict(item)['url'])

        url = dict(item)['url']
        name = re.findall(r'.*/(.*)\?force=download', url)[0]
        sql = 'select url from biying WHERE url="%s"' % url
        cout = self.table.getData(sql=sql, count=1)

        if cout == 0:
            response = requests.get(url, headers=self.heardes)
            with open(r'D:\壁纸\image\%s.jpg' % name, 'wb') as f:
                f.write(response.content)
            data = self.changepanads(dict(item))
            self.table.insertData(data, kind='pandas')

        return item

    def changepanads(self, item):
        """将item数据转换成pandas格式的数据
        """

        name = re.findall(r'.*/(.*)\?force=download', item['url'])[0]

        dataNumPy = np.asarray([(
            item['url'],
            r'D:\壁纸\image\%s.jpg' % name
            )])

        df = pd.DataFrame(dataNumPy, columns=[
            'url',
            'path'
            ])

        return df

