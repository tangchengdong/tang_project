# -*- coding:utf8 -*-
"""读取配置文件信息"""
import os
import yaml

BASEPATH = os.path.dirname(__file__)


def dbConfig():
    data = open(os.path.join(BASEPATH, 'db.default.yaml'), 'r')
    dict = yaml.load(data)
    data.close()
    return dict

 
if __name__ == '__main__':
    print(dbConfig())